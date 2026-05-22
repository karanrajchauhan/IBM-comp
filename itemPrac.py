
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 18:07:56 2019

@author: Karan Raj
"""

import pandas as pd
file= pd.read_csv("D:\PGDBA\Comp\IBM/data.csv")
file.loc[file['Quantity']<0, 'Quantity'] = (-1*file[file['Quantity']<0]['Quantity'])

import matplotlib.pyplot as plt

import seaborn as sns
sns.set()
p=file[file['UnitPrice']<20]['UnitPrice']
plt.hist(File.Quantity)
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()


sns.set()
plt.hist(file['InvoiceDate'])
plt.show()


from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
en=LabelEncoder()
en.fit(file['Country'])
lb=(en.transform(file['Country'])).reshape(len(file['Country']),1)
enc=OneHotEncoder(sparse=False)
enc.fit(lb)
countransform=enc.transform(lb)
trans=pd.concat([file,pd.DataFrame(countransform)],axis=1,sort=False)
trans=trans.drop(['Country','CustomerID','InvoiceDate'],axis=1)
#Items=trans.StockCode.unique()
#mean= trans.groupby(['StockCode'], as_index = False, sort = False).mean().rename(columns = {'Quantity': 'q_mean'})[['StockCode','q_mean']]
#trans = pd.merge(trans,mean,on = 'StockCode', how = 'left', sort = False)
#trans['q_adjusted']=trans['Quantity']-trans['q_mean']
mat=file.pivot_table(values='Quantity',index='StockCode',columns='CustomerID')
from sklearn.neighbors import NearestNeighbors
model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)