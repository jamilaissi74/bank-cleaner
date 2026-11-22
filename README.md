

# bank-cleaner

A command-line tool that cleans messy bank statements (CSV files from several banks) and builds a monthly report of income and expenses by category.

## The problem

Each bank exports its CSV in its own way: different separators, date formats, decimal marks, column names, currencies, blank lines and duplicates. Adding the numbers by hand is slow and error-prone. This tool reads all the files, cleans them into one standard format, sets aside the rows it cannot use (with the reason), and answers two questions:

- How much did I spend and receive each month?
- How much did I spend per category?

## Installation

Requires Python 3.10 or later.

```bash
git clone <your-repo-url>
cd bank-cleaner
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Usage

```bash
python main.py releves/ --out outputs/
```

- `releves/` is the folder containing the bank files (required).
- `--out` is the folder for the results (default: `outputs`). It is created if it does not exist.
- `python main.py --help` shows the options.

The folder must contain the files listed in `file_settings` in `main.py` (`banque_a.csv`, `banque_b.csv`, `banque_c.csv`).

### Output files

| File | Content |
|---|---|
| `report.csv` | Total per month, type (income or expense) and category |
| `rejects.csv` | Rows that could not be cleaned, with the raw values and the reason |
| `duplicates.csv` | Every copy of a duplicated purchase, so you can trace it back to the original line |

Example of `report.csv`:

```csv
date,type,category,amount
2026-01,expense,fuel,-615.89
2026-01,expense,groceries,-46.48
2026-01,income,income,6683.09
```

The column `date` holds a **month** (`YYYY-MM`) and `amount` holds a **total**. Expenses are negative, income is positive.

## How it works

1. **Read** each file with its own settings (separator and decimal mark).
2. **Clean** every row: date, label, amount and currency. A row that fails any check is rejected, with the reason, and the program continues.
3. **Remove duplicates**: rows with the same date, label and amount. The first one is kept.
4. **Categorize** each row from keywords found in its label (see `src/category.py`).
5. **Report**: group by month, type and category, and write the CSV files.

At the end the program prints how many rows were kept, rejected and removed as duplicates.

## Project structure

```
bank-cleaner/
  main.py              command line and main flow
  src/
    cleaning.py        date, label, amount and currency cleaning
    loading.py         read the files and clean each row
    duplicates.py      find and remove duplicates
    category.py        category rules and matching
    report.py          monthly report
  tests/               pytest tests
  releves/             raw bank files (never modified)
  requirements.txt
```

## My choices

- **pandas** to read the CSV files, because it handles different separators and decimal marks with a few settings per file.
- **Settings per file** (a dictionary mapping each file name to its separator and decimal mark), so adding a bank means adding one entry.
- **Dates:** a value with `/` is read as `dd/mm/yyyy`, and a value with `-` as `yyyy-mm-dd`. I checked the files: some `/` dates have a first number above 12, so day first is the only reading that works. Any other format is rejected, not guessed.
- **Amounts** are always converted to MAD, rounded to 2 decimals. An amount in EUR is multiplied by `EUR_TO_MAD` (see `src/cleaning.py`; the rate, its source and its date are noted in the comment). 
- **Labels** are lowercased, accents removed, and spaces replaced by underscores.
- **Income or expense** is decided by the sign of the amount: negative is an expense, positive is income.
- **Categories** use keyword matching: a keyword found anywhere in the label gives the category. The first category in the dictionary that matches wins. A label that matches nothing is categorized as `others`.
- **Duplicates:** same date, label and amount. The first occurrence is kept.
- **Rejected rows** keep the raw values and the reason, so a person can fix the line.
- **Errors are raised by the cleaning functions** and caught in one place (the row loop), so the reason ends up in `rejects.csv`.

## Known limits

- Two real purchases with the same date, label and amount (two identical coffees on the same day) are treated as duplicates, and one is removed.
- `row_index` in `rejects.csv` and `duplicates.csv` is the position in the file's table, not the line number in the original file (the header counts as a line, and blank lines are skipped).
- The exchange rate is fixed. It is not read from a live source.
- Months with no spending in a category have no line in `report.csv`.
- The column order is assumed to be date, label, amount, currency in every file.
- Keyword rules can match more than intended if a keyword is short.
- A positive amount from a shop (a refund) is counted as income.


## Possible next steps

- A readable report (a grid with months across, totals and net, colors for expenses).
- A live exchange rate.
- Detect the separator automatically instead of using a settings table.