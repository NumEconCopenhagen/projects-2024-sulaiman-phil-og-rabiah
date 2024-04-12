from dstapi import DstApi # install with `pip install git+https://github.com/alemartinello/dstapi`


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from matplotlib_venn import venn2
import datetime
import pandas_datareader # install with `pip install pandas-datareader`


# autoreload modules when code is run
%load_ext autoreload
%autoreload 2

# user written modules
import dataproject as dp

#If you dont have the content below, remove the hashtag and install them

 pip install pandas-datareader
 %pip install git+https://github.com/alemartinello/dstapi
 %pip install pandas-datareader

plt.rcParams.update({"axes.grid":True,"grid.color":"black","grid.alpha":"0.25","grid.linestyle":"--"})
plt.rcParams.update({'font.size': 14})

# PRIS111 - First data set
# a. load
PRIS111_api = DstApi('PRIS111') 
params = PRIS111_api._define_base_params(language='en')
PRIS111_true = PRIS111_api.get_data(params=params)

# b. rename and replace
PRIS111_true.rename(columns=columns_dict,inplace=True)

# c. replace data
for key,value in var_dict.items():
   PRIS111_true.variable.replace(key,value,inplace=True)

for key,value in unit_dict.items():
   PRIS111_true.unit.replace(key,value,inplace=True)

# d. keep if in var_dict
I = False
for key,value in var_dict.items():
    I = I | (PRIS111_true.variable == value)
PRIS111_true = PRIS111_true[I]
   
# e. convert values to numeric
PRIS111_true.value = PRIS111_true.value.astype('float')

# d. summary statistics
PRIS111_true.groupby(['variable','unit']).describe()

# f. Sort by year 
PRIS111_true.sort_values(by='year',inplace=True)

# Employment rate in different fields
tabsum_kas= kas.tablesummary(language='en')
display(tabsum_kas)
for var in tabsum_kas['variable name']:
    print(var+':')
    display(kas.variable_levels(var, language='en'))


#Defining parameters
params= {'table': 'kas301',
 'format': 'BULK',
 'lang': 'en',
 'variables': [{'code': 'OMRÅDE', 'values': ['000']},
  {'code': 'BRANCHE07', 'values': ['A', 'H', 'L', 'K', 'CF']},
  {'code': 'SOCIO', 'values': ['02']},
  {'code': 'ALDER', 'values': ['*']},
  {'code': 'KOEN', 'values': ['TOT', 'K', 'M']},
  {'code': 'PERIODE', 'values': ['1']},
  {'code': 'Tid', 'values': ['>2011']}]}
