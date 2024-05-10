import matplotlib.pyplot as plt

def plot_inflation(data):
    plt.figure(figsize=(12, 8))
    plt.plot(data['Year'], data['Inflation rate'], marker='o', linestyle='-', color='blue', label='Inflation')
    plt.title('Inflation from 2007 to 2022')
    plt.xlabel('Year')
    plt.ylabel('Inflation Percentage')
    plt.xticks(data['Year'].unique(), rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()

import matplotlib.pyplot as plt

def plot_merged_data(Combined_data):
    plt.figure(figsize=(12, 8))
    plt.plot(Combined_data['Year'], Combined_data['Inflation rate'], marker='o', linestyle='-', color='blue', label='Inflation')
    plt.plot(Combined_data['Year'], Combined_data['Unemployment'], marker='x', linestyle='--', color='green', label='Unemployment')
    plt.title('Inflation and Unemployment from 2007 to 2022')
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.xticks(Combined_data['Year'].unique(), rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()


import matplotlib.pyplot as plt

def plot_real_gdp(GDP):
    plt.figure(figsize=(10, 4))
    plt.plot(GDP['Year'], GDP['Real GDP'], marker='o', color='blue')
    plt.ylabel('Real GDP (Mia. kr.)')
    plt.title('Real GDP Over Time in Denmark')
    plt.xlabel('Year')
    plt.grid(True)  # Add gridlines
    plt.tight_layout()
    plt.show()

def plot_graph(x, y, title='title', xlabel='xlabel', ylabel='ylabel', label_a='label_a'):
    """ docstrings """
    plt.figure(figsize=(12, 8))
    plt.plot(x, y, marker='o', linestyle='-', color='blue', label=label_a)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_graph_2(x1,x2, y1,y2, title='title', xlabel='xlabel', ylabel='ylabel', label_a='label_a', label_b='label_b'):
    """ docstrings """
    plt.figure(figsize=(12, 8))
    plt.plot(x1, y1, marker='o', linestyle='-', color='blue', label=label_a)
    plt.plot(x2, y2, marker='x', linestyle='--', color='green', label=label_b)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()