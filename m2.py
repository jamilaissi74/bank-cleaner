import pandas as pd
import os     


df = pd.read_csv('./releves/banque_c.csv')
print(len(df))
#print(df.head())
#print(df.shape)
#print(df.columns)
s=['a','b','c']
for i in range(len(s)):
    print('file name : banque_'+s[i]+'.csv: ')
    print(len(pd.read_csv('./releves/banque_'+s[i]+'.csv')))

dirlist= os.listdir('./releves')
for i in range(len(dirlist)):
    print('file name : '+dirlist[i]+': ')
    print(len(pd.read_csv('./releves/'+dirlist[i])))