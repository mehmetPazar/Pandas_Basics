# -*- coding: utf-8 -*-

import pandas as pd

dictionary = { "Name":["ali","veli","mehmet","ayşe","fatma"],
               "Age":[18,20,35,46,82],
               "Maas":[1200,1380,1349,5000,2365]}

dataFrame1 = pd.DataFrame(dictionary)

head = dataFrame1.head(3)
tail = dataFrame1.tail()

print(dataFrame1)
print(head)

#%%

print(dataFrame1.columns)
print(dataFrame1.info())
print(dataFrame1.dtypes)
print(dataFrame1.describe())

#%%

print(dataFrame1["Name"])
print(dataFrame1["Age"])
print(dataFrame1.Age)

dataFrame1["new_feature"] = [-1,-2,-3,-4,-5] 
print(dataFrame1)
print(dataFrame1.new_feature)

print(dataFrame1.loc[:,"Name"])
print(dataFrame1.loc[:3,"Name"])

print(dataFrame1.loc[1:3,"Name":"Maas"])
print(dataFrame1.loc[1:3,["Name","Maas"]])

print(dataFrame1.loc[::-1,:])
print(dataFrame1.loc[:,:"Age"])

print(dataFrame1.iloc[:,2])
print(dataFrame1.iloc[:,:3])

#%%

filtre1 = dataFrame1.Maas > 2000
print(filtre1)
print(type(filtre1))

filtrelenmis_data = dataFrame1[filtre1]
print(filtrelenmis_data)

filtre2 = dataFrame1.Age < 47
print(dataFrame1[filtre2])

print(dataFrame1[filtre1 & filtre2])

print(dataFrame1[dataFrame1.Maas < 2300 ])


#%%
import numpy as np

ortalama_maas = dataFrame1.Maas.mean()
print(ortalama_maas)

ortalama_maas_np = np.mean(dataFrame1.Maas)
print(ortalama_maas_np)

dataFrame1["Maas_seviyesi"] = ["dusuk "if ortalama_maas > each else "yuksek" for each in dataFrame1.Maas]
print(dataFrame1)


dataFrame1.columns = [ each.upper() for each in dataFrame1.columns]
print(dataFrame1.columns)


#%%

#dataFrame1.drop(["NEW_FEATURE"] , axis = 1 , inplace=True) 
#print(dataFrame1)

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

data_concat = pd.concat([data1,data2],axis=0)
print(dataFrame1.head())

maas = dataFrame1.MAAS
name = dataFrame1.NAME
data_concat = pd.concat([maas,name],axis=1)
print(data_concat)

#%%

dataFrame1["AGE_SQR"] = [each*each for each in dataFrame1.AGE]
print(dataFrame1)


def multiply(age):
    return age*2

dataFrame1["apply_metodu"] = dataFrame1.AGE.apply(multiply)
print(dataFrame1) 












