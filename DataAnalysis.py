import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\hp\Downloads\ToyotaCorolla1[1].csv",header='infer')
print('shape of data:',data.shape)
print('null values:',data.isnull().sum().sum())#1b
unique_values=data.apply(pd.Series.nunique)#1b
print(unique_values)#1b
print(data.info())#1d,1e

imp_data=data.iloc[:,2:]
num_data = imp_data.select_dtypes(include=['number'])
print("shape of data",data.shape)
print("shape of imp_data",imp_data.shape)
print("shape of num_data",num_data.shape)

for column in num_data.columns:
    print(column)
    print("Sum:",num_data[column].sum())
    print("min:",num_data[column].min())
    print("max:",num_data[column].max())
    print("range:",num_data[column].max()-num_data[column].min())
    print("Mean:",num_data[column].mean())
    print("median:",num_data[column].median())
    print("Standard deviation",num_data[column].std())
    print("variance:",num_data[column].var())
    print()
    
print()

for column in num_data.columns:
    print(column)
    print("(mode):",data[column].mode()[0])
    print("unique Values:",data[column].unique())
    print("unique value counts:",len(data[column].unique()))
    print()

plot_data = data.select_dtypes(include=['number'])
print(plot_data.info())


x_value = plot_data.iloc[:,0]
y_price = plot_data.iloc[:,1]
plt.plot(x_value, y_price, '.')
plt.xlabel('Index numbers')
plt.ylabel('Price')
plt.title('The Plot: Price and Index')
plt.grid(True)
plt.show()

y_price = plot_data.iloc[:,1]
x_age = plot_data.iloc[:,2]
plt.scatter(x_age, y_price, color='r', marker='.')
plt.ylabel('Price')
plt.title('The Plot: Age and Price')
plt.grid(True)
plt.show()

plot_data['Mfg_Month'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Manufacturing Month Distribution')
plt.xlabel('Month')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

data['Fuel_Type'].value_counts().sort_index().plot(kind='pie')
plt.title('Fuel types')
plt.ylabel('', fontsize=12)
plt.show()

data['Color'].value_counts().sort_index().plot(kind='pie',fontsize=7)
plt.title('Colors')
plt.ylabel('', fontsize=12)
plt.show()
