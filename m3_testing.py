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

print(cleaning.currency_normalizing("EUR"))
print(cleaning.currency_normalizing("MAD"))