import pandas as pd
from src import cleaning 
import os

file_settings={
    'banque_a.csv': {'decimal': '.', 'delimiter': ','},
    'banque_b.csv': {'decimal': ',', 'delimiter': ';'},
    'banque_c.csv': {'decimal': '.', 'delimiter': ','}
}

list_normalized=[]
rejected_rows=[]

for key, value in file_settings.items():
    df=pd.read_csv('./releves/'+key, **value)
    print('file name : '+key+': ')

    for row in df.itertuples():
        try:
            cleaned_row={
                'file_name': key,
                'date': cleaning.date_normalizing(row[1]),
                'label': cleaning.label_normalizing(row[2]),
                'amount': cleaning.amount_cleaning(row[3], row[4]),
                'currency': cleaning.currency_normalizing(row[4])
            }
            print("AFTER CLEANING \n", cleaned_row)
            list_normalized.append(cleaned_row)
        except ValueError as e:
            error_decitionary = {
                'file_name' : key,
                'row_index': row[0] , #this give the index of the row in the original dataframe not the line from file
                'reason': e,
                'date': row[1],
                'label': row[2],
                'amount': row[3],
            }
            print("REJECTED ROW \n", row, "\nREASON: ", e)
            rejected_rows.append(error_decitionary)

  
        

        try:
            os.makedirs('./outputs', exist_ok=False)
            print("directory created")
        except FileExistsError:
            print("directory already exists")
    df_rejects= pd.DataFrame(rejected_rows)
    df_rejects.to_csv('./outputs/rejects.csv', index=False)



