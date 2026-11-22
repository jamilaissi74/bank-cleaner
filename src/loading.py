import pandas as pd 
import os 
from src import cleaning      # keep your own imports

def loading(input_folder, file_settings, output_folder):
    list_normalized=[]
    rejected_rows=[]

    for key, value in file_settings.items():
        df=pd.read_csv(os.path.join(input_folder, key), **value)
    
        for row in df.itertuples():
            try:
                cleaned_row={
                    'file_name': key,
                    'original_row': row[0],
                    'date': cleaning.date_normalizing(row[1]),
                    'label': cleaning.label_normalizing(row[2]),
                    'amount': cleaning.amount_cleaning(row[3], row[4]),
                }

                list_normalized.append(cleaned_row)
            except ValueError as e:
                error_decitionary = {
                    'file_name' : key,
                    'row_index': row[0] , #this give the index of the row in the original dataframe not the line from file
                    'reason': e,
                    'date': row[1],
                    'label': row[2],
                    'amount': row[3],
                    'currency': row[4]
                }

                rejected_rows.append(error_decitionary)
    
    
    df_rejects= pd.DataFrame(rejected_rows)
    df_rejects.to_csv(os.path.join(output_folder, 'rejects.csv'), index=False)
    df_cleaned=pd.DataFrame(list_normalized)
    return df_cleaned