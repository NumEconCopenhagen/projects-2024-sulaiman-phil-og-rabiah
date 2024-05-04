import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas_datareader # install with `pip install pandas-datareader`
from dstapi import DstApi # install with `pip install git+https://github.com/alemartinello/dstapi`

# user written modules
import dataproject as dp

def inf_fig(x, y, color='blue', label='y', legend_pos='best'):
  
  Returns: 
  matplotlib.figure.Figure: 
  
plt.figure(figsize=(12, 8))
plt.plot(PRIS111['Year'], PRIS111['Inflation rate'], marker='o', linestyle='-', color='blue', label='Inflation')
plt.title('Inflation from 2007 to 2022')
plt.xlabel('Year')
plt.ylabel('Inflation Percentage')
plt.xticks(PRIS111['Year'].unique(), rotation=45)
plt.legend()
plt.grid(True)
plt.show();




