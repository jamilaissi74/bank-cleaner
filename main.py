import argparse
import os
import sys

import pandas as pd
from src import category,loading ,duplicates, report

file_settings = {                        # stays here, outside main
    'banque_a.csv': {'decimal': '.', 'delimiter': ','},
    'banque_b.csv': {'decimal': ',', 'delimiter': ';'},
    'banque_c.csv': {'decimal': '.', 'delimiter': ','},
}


def main(input_folder, output_folder):
    if not os.path.isdir(input_folder):
        print(f"Error: input folder not found: {input_folder}")
        sys.exit(1)

    os.makedirs(output_folder, exist_ok=True)

    cleaned_df=loading.loading(input_folder, file_settings, output_folder)

    df_no_duplicates=duplicates.split_duplicates(cleaned_df, output_folder)
    #----------------M6-----------------------------

    df=category.add_category(df_no_duplicates)


    #------------------M7---------------------
    report.build_report(df, output_folder)
    print("\nDone.")
    # print(f"Rows kept: {len(df_no_duplicates)}")
    # print(f"Rows rejected: {len(rejected_rows)}")
    # print(f"Duplicates removed: {len(df_cleaned) - len(df_no_duplicates)}")
    # print(f"Results are in: {output_folder}")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Clean bank statements and build a monthly report.")
    parser.add_argument("input_folder",
                        help="folder containing the bank CSV files")
    parser.add_argument("--out", default="outputs",
                        help="folder for the results (default: outputs)")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    main(args.input_folder, args.out)