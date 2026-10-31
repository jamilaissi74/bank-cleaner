import pandas as pd
import os     


#df = pd.read_csv('./releves/banque_b.csv', delimiter=';')
#print(len(df))
#print(df.head())
#print(df.shape)
#print(df.columns)


file_settings={
    'banque_a.csv': {'decimal': '.', 'delimiter': ','},
    'banque_b.csv': {'decimal': ',', 'delimiter': ';'},
    'banque_c.csv': {'decimal': '.', 'delimiter': ','}
}

# df=pd.read_csv('./releves/banque_b.csv', **file_settings['banque_b.csv'])
# print(df.dtypes)
# print(len(df))
# print(df.shape)
# print(df.columns)
# print(df.head(3))

# df=pd.read_csv('./releves/banque_a.csv', **file_settings['banque_a.csv'])
# print(df.dtypes)
# print(len(df))
# print(df.shape)
# print(df.columns)
# print(df.head(3))

# df=pd.read_csv('./releves/banque_c.csv', **file_settings['banque_c.csv'])
# print(df.dtypes)
# print(len(df))
# print(df.shape)
# print(df.columns)
# print(df.head(3))

for key, value in file_settings.items():
    df=pd.read_csv('./releves/'+key, **value)
    print('file name : '+key+': ')
    print(df.dtypes)
    print(len(df))
    print(df.shape)
    print(df.columns)
    print(df.head(3))

# dirlist= os.listdir('./releves')
# for i in range(len(dirlist)):
#     if pd.read_csv('./releves/'+dirlist[i]). != 6:
#     print('file name : '+dirlist[i]+': ')
#     df=pd.read_csv('./releves/'+dirlist[i], decimal=',', delimiter=';',engine='python')
#     print(df.dtypes)
#     print(len(df))
#     print(df.shape)
#     print(df.columns)
#     #print(df.head())
#     print(df.head(3))
