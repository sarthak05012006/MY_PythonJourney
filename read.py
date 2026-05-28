import pandas 
import numpy as np
import matplotlib.pyplot as plt
"""
read data from file into a datafram
df = pd.read_csv(")
df = pd.read_excel(")"""
df = pandas.read_json("/Users/sarthakdewangan/Documents/python/pandas/sample_Data.json")
print(df)  
print(df.head(2))
print(df.info())
print(df.describe())
df.plot()
plt.show()
