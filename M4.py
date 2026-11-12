import pandas as pd
from src import cleaning 
df= pd.read_csv('./releves/banque_a.csv', decimal='.', delimiter=',')



list_normalized=[]
rejected_rows=[]
for row in df.itertuples():
    try:
    
        date_pc= cleaning.date_normalizing(row.date)
        label_pc= cleaning.label_normalizing(row.libelle)
        currency_pc= cleaning.currency_normalizing(row.devise)
        amount_pc= cleaning.amount_cleaning(row.montant, row.devise)
        b=[date_pc, label_pc, amount_pc, currency_pc]
        print("AFTER CLEANING \n", b)
        list_normalized.append(b)
    except ValueError as e:
        error_decitionary = {
            'file_name' : "banque_a.csv",
            'row_index': row[0] , #this give the index of the row in the original dataframe not the line from file
            'reason': e,
            'raw_data': row,
        }
        print("REJECTED ROW \n", row, "\nREASON: ", e)
        rejected_rows.append(error_decitionary)

print("list length", len(list_normalized))
print("rejected rows length", len(rejected_rows))
print("rejected rows", rejected_rows)