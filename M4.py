import pandas as pd
from src import cleaning 
df= pd.read_csv('./releves/banque_a.csv', decimal='.', delimiter=',')

list_normalized=[]
rejected_rows=[]
for row in df.itertuples():
    try:
    
        date= cleaning.date_normalizing(row.date)
        label= cleaning.label_normalizing(row.libelle)
        currency= cleaning.currency_normalizing(row.devise)
        amount= cleaning.amount_cleaning(row.montant, row.devise)
        b=[date, label, amount, currency]
        print("AFTER CLEANING \n", b)
        list_normalized.append(b)
    except ValueError as e:
        print("REJECTED ROW \n", row, "\nREASON: ", e)
        rejected_rows.append(row)

print("list length", len(list_normalized))
print("rejected rows length", len(rejected_rows))
