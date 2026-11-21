import pandas as pd
from src import cleaning, category
import os
from collections import OrderedDict as ordered

file_settings={
    'banque_a.csv': {'decimal': '.', 'delimiter': ','},
    'banque_b.csv': {'decimal': ',', 'delimiter': ';'},
    'banque_c.csv': {'decimal': '.', 'delimiter': ','}
}

list_normalized=[]
rejected_rows=[]

for key, value in file_settings.items():
    df=pd.read_csv('./releves/'+key, **value)
    # print('file name : '+key+': ')

    for row in df.itertuples():
        try:
            cleaned_row={
                'file_name': key,
                'original_row': row[0],
                'date': cleaning.date_normalizing(row[1]),
                'label': cleaning.label_normalizing(row[2]),
                'amount': cleaning.amount_cleaning(row[3], row[4]),
            }
            # print("AFTER CLEANING \n", cleaned_row)
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
            # print("REJECTED ROW \n", row, "\nREASON: ", e)
            rejected_rows.append(error_decitionary)

  
        

os.makedirs('./outputs', exist_ok=True)
df_rejects= pd.DataFrame(rejected_rows)
df_rejects.to_csv('./outputs/rejects.csv', index=False)



#---------------------M5---------------------------

df_cleaned=pd.DataFrame(list_normalized)
# print("Number of rows after cleaning: ", len(df_cleaned))

duplicated_rows=[]

duplicated_df=df_cleaned.duplicated(subset=['date', 'label', 'amount'], keep=False)
for index, is_duplicated in duplicated_df.items():
    if is_duplicated:
        duplicated_row=df_cleaned.iloc[index]
        error_decitionary = {
            'file_name' : duplicated_row['file_name'],
            'row_index':duplicated_row['original_row'] ,
            'reason': "duplicate row",
            'date': duplicated_row['date'],
            'label': duplicated_row['label'],
            'amount': duplicated_row['amount'],
        }
        # print("DUPLICATED ROW \n", duplicated_row, "\nREASON: ", "duplicate row")
        duplicated_rows.append(error_decitionary) 

df_no_duplicates=df_cleaned.drop_duplicates(subset=['date', 'label', 'amount'], keep='first')

 
# print("total",len(df_cleaned))
# print("Number of unique rows after cleaning: ", len(df_no_duplicates))
# print("Number of duplicated rows: ", len(duplicated_rows))

os.makedirs('./outputs', exist_ok=True)
df_duplicated= pd.DataFrame(duplicated_rows)
df_duplicated.to_csv('./outputs/duplicates.csv', index=False)

#----------------M6-----------------------------

print(df_no_duplicates['label'].unique())
categories=[]
for row_m6 in df_no_duplicates.itertuples():
    categories.append(category.categorize(row_m6.label))

df_no_duplicates ['category']=categories
print(df_no_duplicates.head())


#------------------M7---------------------
final_date=pd.to_datetime(df_no_duplicates['date']).dt.to_period('M')
report_df=pd.DataFrame(final_date)
print(report_df)

amount_type=[]
for final_amount in df_no_duplicates['amount'] :
    if final_amount < 0 :
        amount_type.append("expense")
    else:
        amount_type.append("income")

report_df['type']=amount_type
report_df['amount']=df_no_duplicates['amount']
report_df['category']=df_no_duplicates['category']

print(report_df)
#print(report_df.groupby(['date','type','category']).sum())
#detail = report_df.groupby(['date', 'type', 'category']).sum().reset_index()
detail=report_df.groupby(['date', 'type', 'category']).sum().reset_index()
print(detail)
detail.to_csv('./outputs/reports.csv', index=False, float_format="%.2f")