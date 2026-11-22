import pandas as pd 
import os 
from src import cleaning, category

def split_duplicates(cleaned_df, ouput_folder ):
    duplicated_rows=[]
    
    duplicated_df=cleaned_df.duplicated(subset=['date', 'label', 'amount'], keep=False)
    for index, is_duplicated in duplicated_df.items():
        if is_duplicated:
            duplicated_row=cleaned_df.iloc[index]
            error_decitionary = {
                'file_name' : duplicated_row['file_name'],
                'row_index':duplicated_row['original_row'] ,
                'reason': "duplicate row",
                'date': duplicated_row['date'],
                'label': duplicated_row['label'],
                'amount': duplicated_row['amount'],
            }
            duplicated_rows.append(error_decitionary) 
    
    df_no_duplicates=cleaned_df.drop_duplicates(subset=['date', 'label', 'amount'], keep='first')
    
    df_duplicated= pd.DataFrame(duplicated_rows)
    df_duplicated.to_csv(os.path.join(ouput_folder, 'duplicates.csv'), index=False)
    return df_no_duplicates