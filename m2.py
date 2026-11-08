import pandas as pd     


file_settings={
    'banque_a.csv': {'decimal': '.', 'delimiter': ','},
    'banque_b.csv': {'decimal': ',', 'delimiter': ';'},
    'banque_c.csv': {'decimal': '.', 'delimiter': ','}
}

for key, value in file_settings.items():
    df=pd.read_csv('./releves/'+key, **value)
    print('file name : '+key+': ')
    print(df.dtypes)
    print(len(df))
    print(df.shape)
    print(df.columns)
    print(df.head(3))
