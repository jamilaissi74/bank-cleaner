import re

from src import cleaning
import pandas as pd
from datetime import date


# df = pd.read_csv('./releves/banque_a.csv',usecols=[1], decimal='.', delimiter=',')

# for label in df.items():
#     print("original :", label)
#     b = cleaning.label_normalizing(label)
#     print("output :", b, "\n")

text= "CARREFOUR MARKET"
# a=cleaning.label_normalizing(text)
# print(a)

# print(cleaning.label_normalizing("NETFLIX"))
# print(cleaning.label_normalizing("Netflix"))
# print(cleaning.label_normalizing("  CTM VOYAGE  "))
# print(cleaning.label_normalizing("CTM   VOYAGE"))
# print(cleaning.label_normalizing(""))
# print(cleaning.label_normalizing("   "))
# print(cleaning.label_normalizing(None))
# print(df)
# labels_a = df
# for i in range(len(labels_a)) :
#     print("index :", i)
#     print("original :", labels_a )
#     #b = cleaning.label_normalizing(labels_a[i])
#     #print("output :", b, "\n")

# df = pd.read_csv('./releves/banque_b.csv', decimal=',', delimiter=';')




# # for x in df['Date operation']:
# #     print("original :", x)
# #     b = cleaning.date_normalizing(x)
# #     print("output :", b, "\n")

# tests = [
#     ("03/04/2026", date(2026, 4, 3)),    # 3 April, not 4 March
#     ("10/06/2026", date(2026, 6, 10)),   # 10 June, not 6 October
#     ("01/02/2026", date(2026, 2, 1)),    # 1 February
#     ("13/04/2026", date(2026, 4, 13)),
#     ("2026-04-03", date(2026, 4, 3)),    # ISO, same date as the first
#     ("2026-06-10", date(2026, 6, 10)),
#     ("  2026-04-03  ", date(2026, 4, 3)),  # spaces around
#     ("2026-02-30", None),                # day out of range
#     ("31/04/2026", None),                # April has 30 days
#     ("2026-13-01", None),                # month 13
#     ("abc", None),
#     ("", None),
#     ("   ", None),
#     (None, None),
# ]

# for value, expected in tests:
#     try:
#         result = cleaning.date_normalizing(value)
#         status = "OK" if result == expected else "WRONG"
#         print(status, repr(value), "->", result, "(expected", expected, ")")
#     except ValueError as e:
#         status = "OK" if expected is None else "WRONG"
#         print(status, repr(value), "-> REJECTED:", e)

# print(cleaning.currency_normalizing("EUR"))
# print(cleaning.currency_normalizing("MAD"))
# print(cleaning.amount_cleaning("100"))  # Should return 1234.56




def check(function, args, expected):
    """expected = a value, or 'REJECT' if the function must raise ValueError."""
    try:
        result = function(*args)
        ok = (expected != "REJECT") and (result == expected)
        print("OK   " if ok else "WRONG", args, "->", result, "| expected:", expected)
    except ValueError as e:
        ok = expected == "REJECT"
        print("OK   " if ok else "WRONG", args, "-> REJECTED:", e)


print("--- LABEL ---")
check(cleaning.label_normalizing, ("NETFLIX",), "netflix")
check(cleaning.label_normalizing, ("Netflix",), "netflix")          # same as above
check(cleaning.label_normalizing, ("  CTM VOYAGE  ",), "ctm_voyage")
check(cleaning.label_normalizing, ("CTM   VOYAGE",), "ctm_voyage")
check(cleaning.label_normalizing, ("",), "REJECT")
check(cleaning.label_normalizing, ("   ",), "REJECT")
check(cleaning.label_normalizing, (None,), "REJECT")
check(cleaning.label_normalizing, (float("nan"),), "REJECT")
# accent: no expected value, it depends on YOUR decision. Just look at it.
print("accent test:", cleaning.label_normalizing("Café Hafa"), "|", cleaning.label_normalizing("CAFE HAFA"))

print("--- AMOUNT ---")
check(cleaning.amount_cleaning, ("-119,91", "MAD"), -119.91)
check(cleaning.amount_cleaning, ("-622.32", "MAD"), -622.32)
check(cleaning.amount_cleaning, (-94.12, "mad "), -94.12)           # already a number
check(cleaning.amount_cleaning, ("1 234,50", "MAD"), 1234.5)
check(cleaning.amount_cleaning, ("100", "MAD"), 100.0)
check(cleaning.amount_cleaning, ("-100,00", "EUR"), round(-100 * cleaning.EUR_TO_MAD, 2))
check(cleaning.amount_cleaning, ("-100,00", "eur "), round(-100 * cleaning.EUR_TO_MAD, 2))
check(cleaning.amount_cleaning, ("ab", "MAD"), "REJECT")
check(cleaning.amount_cleaning, ("", "MAD"), "REJECT")
check(cleaning.amount_cleaning, (None, "MAD"), "REJECT")
check(cleaning.amount_cleaning, (float("nan"), "MAD"), "REJECT")
check(cleaning.amount_cleaning, ("-100,00", "USD"), "REJECT")
check(cleaning.amount_cleaning, ("-100,00", ""), "REJECT")

print("--- FILE C, row by row ---")
df = pd.read_csv("./releves/banque_c.csv")
for i, row in df.iterrows():
    try:
        cleaning.amount_cleaning(row["montant"], row["devise"])
    except ValueError as e:
        print("rejected row", i, "|", row["montant"], row["devise"], "|", e)