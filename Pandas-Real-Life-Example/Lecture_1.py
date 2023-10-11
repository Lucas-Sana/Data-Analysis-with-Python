import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregando o conjunto de dados de vendas
sales = pd.read_csv('data/sales_data.csv', parse_dates=['Date'])

# Explorando o conjunto de dados
sales.head()
sales.shape
sales.info()
sales.describe()

# Análise numérica e visualização
sales['Unit_Cost'].describe()
sales['Unit_Cost'].mean()
sales['Unit_Cost'].median()
sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,6))
sales['Unit_Cost'].plot(kind='density', figsize=(14,6))  # KDE
ax = sales['Unit_Cost'].plot(kind='density', figsize=(14,6))  # KDE
ax.axvline(sales['Unit_Cost'].mean(), color='red')
ax.axvline(sales['Unit_Cost'].median(), color='green')
ax = sales['Unit_Cost'].plot(kind='hist', figsize=(14,6))
ax.set_ylabel('Número de Vendas')
ax.set_xlabel('Dólares')

# Análise categórica e visualização
sales['Age_Group'].value_counts()
sales['Age_Group'].value_counts().plot(kind='pie', figsize=(6,6))
ax = sales['Age_Group'].value_counts().plot(kind='bar', figsize=(14,6))
ax.set_ylabel('Número de Vendas')

# Relacionamento entre as colunas
corr = sales.corr()
fig = plt.figure(figsize=(8,8))
plt.matshow(corr, cmap='RdBu', fignum=fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical');
plt.yticks(range(len(corr.columns)), corr.columns);
sales.plot(kind='scatter', x='Customer_Age', y='Revenue', figsize=(6,6))
sales.plot(kind='scatter', x='Revenue', y='Profit', figsize=(6,6))
ax = sales[['Profit', 'Age_Group']].boxplot(by='Age_Group', figsize=(10,6))
ax.set_ylabel('Lucro')
boxplot_cols = ['Year', 'Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Profit']
sales[boxplot_cols].plot(kind='box', subplots=True, layout=(2,3), figsize=(14,8))

# Manipulação de colunas
sales['Revenue_per_Age'] = sales['Revenue'] / sales['Customer_Age']
sales['Revenue_per_Age'].plot(kind='density', figsize=(14,6))
sales['Revenue_per_Age'].plot(kind='hist', figsize=(14,6))
sales['Calculated_Cost'] = sales['Order_Quantity'] * sales['Unit_Cost']
sales['Calculated_Cost'].head()
(sales['Calculated_Cost'] != sales['Cost']).sum()
sales.plot(kind='scatter', x='Calculated_Cost', y='Profit', figsize=(6,6))
sales['Calculated_Revenue'] = sales['Cost'] + sales['Profit']
sales['Calculated_Revenue'].head()
(sales['Calculated_Revenue'] != sales['Revenue']).sum()
sales['Revenue'].plot(kind='hist', bins=100, figsize=(14,6))
sales['Unit_Price'] *= 1.03

# Seleção e Indexação
sales.loc[sales['State'] == 'Kentucky']
sales.loc[sales['Age_Group'] == 'Adults (35-64)', 'Revenue'].mean()
sales.loc[(sales['Age_Group'] == 'Youth (<25)') | (sales['Age_Group'] == 'Adults (35-64)')].shape[0]
sales.loc[(sales['Age_Group'] == 'Adults (35-64)') & (sales['Country'] == 'United States'), 'Revenue'].mean()
sales.loc[sales['Country'] == 'France', 'Revenue'] *= 1.1
