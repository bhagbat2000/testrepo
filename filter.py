# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:20:28 2020

@author: Bhagabat
"""

# data exploration, selection and Filtration
import pandas as pd 
df = pd.read_csv(r"C:\Users\Bhagabat\Desktop\datawh.csv",index_col=['Dates'])
'''
exploration - understand data,collect information,identify,challenge in data
'''
df.shape
print(df.columns)
df.head()#ttop rows
df.head(2)#top 2 rows
df.tail(2)

df.info()
df.info()
df.describe()


###############################################################################
df.head()
df['Temperature']
df.Temperature# not recomeded 
df[['Temperature','Humidity']]

type(df['Temperature'])
type(df[['Temperature','Humidity']])

df['05-05-2018':'12-05-2018']['Temperature']
df['05-05-2018':'12-05-2018'][['Temperature','Humidity']]
###############################################################################
#filtering '
df[df.Temperature>2000]
df[df['Temperature']>2000]
df[df['Temperature']>2000][['Temperature','Humidity']]

#and

df.describe()
df['Temperature'].mean()
df['Temperature'].median()
df['Temperature'].mode()
df['Temperature'].min()
df['Temperature'].max()
df['Temperature'].var()#variance
df['Temperature'].std()
df['Temperature'].skew()















