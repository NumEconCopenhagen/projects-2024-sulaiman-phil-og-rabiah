from dstapi import DstApi # install with `pip install git+https://github.com/alemartinello/dstapi`


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from matplotlib_venn import venn2
import datetime
import pandas_datareader # install with `pip install pandas-datareader`

#If you dont have the content below, remove the hashtag and install them

# PRIS111 - First data set
# a. load
# PRIS111_api = DstApi('PRIS111') 
# params = PRIS111_api._define_base_params(language='en')
# PRIS111_true = PRIS111_api.get_data(params=params)

# b. rename and replace
# PRIS111_true.rename(columns=columns_dict,inplace=True)

# c. replace data
# for key,value in var_dict.items():
   #PRIS111_true.variable.replace(key,value,inplace=True)

#for key,value in unit_dict.items():
   #PRIS111_true.unit.replace(key,value,inplace=True)

# d. keep if in var_dict
#I = False
#for key,value in var_dict.items():
    #I = I | (PRIS111_true.variable == value)
#PRIS111_true = PRIS111_true[I]
   
# e. convert values to numeric
#PRIS111_true.value = PRIS111_true.value.astype('float')

# d. summary statistics
#PRIS111_true.groupby(['variable','unit']).describe()

# f. Sort by year 
#PRIS111_true.sort_values(by='year',inplace=True)
