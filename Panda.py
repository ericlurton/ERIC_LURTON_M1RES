#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

#lecture csv

data = pd.read_csv('mower_market_snapshot.csv', sep=";")

total_nan_values = snapshot.isnull().sum()
total_nan_values


# In[ ]:


total_nan_values = snapshot.isnull().sum().sum()
total_nan_values


# In[ ]:


#Remplacement des valeurs vide ( unknow ) par la moyenne ( prod_cost )

data = data.replace('unknown', np.nan) 

data['prod_cost'] = pd.to_numeric(data['prod_cost'])
print(data['prod_cost'])
data['prod_cost'] = data['prod_cost'].replace(np.nan, data['prod_cost'].mean())
print(data['prod_cost'])


# In[1]:


#Afficher les valeurs unique de la colonne waranty
def warranty():
    
    data = pd.read_csv('mower_market_snapshot.csv', sep=";")
    data['warranty'] = pd.to_numeric(data['warranty'].str[0])
    print(data['warranty'])
    
warranty()


# In[ ]:


#Création des 3 colonnes 

df = pd.read_csv('mower_market_snapshot.csv', sep=";")
df = pd.get_dummies(df.product_type, prefix='product_type')
df.head()

#Transformer la colonne product_type en colonne numérique avec 3 catégorie "1, 2 et 3"


# In[ ]:


data = pd.read_csv('mower_market_snapshot.csv', sep=";")
data.product_type = pd.Categorical(data.product_type)
data['product_type'] = data.product_type.cat.codes
data['product_type'] = pd.factorize(data['product_type'])[0] + 1
print(data['product_type'])

