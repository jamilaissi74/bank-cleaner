import pandas as pd 
import os 

def build_report(df, output_folder):
    final_date=pd.to_datetime(df['date']).dt.to_period('M')
    report_df=pd.DataFrame(final_date)
    print(report_df)
    
    amount_type=[]
    for final_amount in df['amount'] :
        if final_amount < 0 :
            amount_type.append("expense")
        else:
            amount_type.append("income")
    
    report_df['type']=amount_type
    report_df['amount']=df['amount']
    report_df['category']=df['category']
    
    #print(report_df.groupby(['date','type','category']).sum())
    #detail = report_df.groupby(['date', 'type', 'category']).sum().reset_index()
    detail=report_df.groupby(['date', 'type', 'category']).sum().reset_index()

    detail.to_csv(os.path.join(output_folder, 'report.csv'), index=False, float_format="%.2f")
    return detail