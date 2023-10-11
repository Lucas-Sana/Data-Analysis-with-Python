import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos dados
sales = pd.read_csv('data/sales_data.csv', parse_dates=['Date'])

# Qual é a média da 'Customer_Age'?
sales['Customer_Age'].mean()

# Gráfico de densidade (KDE) e box plot para 'Customer_Age'
sales['Customer_Age'].plot(kind='kde', figsize=(14,6))
sales['Customer_Age'].plot(kind='box', vert=False, figsize=(14,6))

# Qual é a média da 'Order_Quantity'?
sales['Order_Quantity'].mean()

# Histograma e box plot para 'Order_Quantity'
sales['Order_Quantity'].plot(kind='hist', bins=30, figsize=(14,6))
sales['Order_Quantity'].plot(kind='box', vert=False, figsize=(14,6))

# Quantas vendas foram feitas por ano?
sales['Year'].value_counts()

# Gráfico de pizza para as vendas por ano
sales['Year'].value_counts().plot(kind='pie', figsize=(6,6))

# Quantas vendas foram feitas por mês?
sales['Month'].value_counts()

# Gráfico de barras para as vendas por mês
sales['Month'].value_counts().plot(kind='bar', figsize=(14,6))

# Qual país teve mais vendas em termos de quantidade?
sales['Country'].value_counts()

# Gráfico de barras para as vendas por país
sales['Country'].value_counts().plot(kind='bar', figsize=(14,6))

# Lista de todos os produtos vendidos
sales['Product'].unique()

# Gráfico de barras para os 10 produtos mais vendidos
sales['Product'].value_counts().head(10).plot(kind='bar', figsize=(14,6))

# Gráfico de dispersão entre 'Unit_Cost' e 'Unit_Price'
sales.plot(kind='scatter', x='Unit_Cost', y='Unit_Price', figsize=(6,6))

# Gráfico de dispersão entre 'Order_Quantity' e 'Profit'
sales.plot(kind='scatter', x='Order_Quantity', y='Profit', figsize=(6,6))

# Box plot agrupado por país para 'Profit'
sales[['Profit', 'Country']].boxplot(by='Country', figsize=(10,6))

# Box plot agrupado por país para 'Customer_Age'
sales[['Customer_Age', 'Country']].boxplot(by='Country', figsize=(10,6))

# Adição da coluna 'Calculated_Date'
sales['Calculated_Date'] = sales[['Year', 'Month', 'Day']].apply(lambda x: '{}-{}-{}'.format(x[0], x[1], x[2]), axis=1)

# Conversão de 'Calculated_Date' para datetime
sales['Calculated_Date'] = pd.to_datetime(sales['Calculated_Date'])

# Gráfico de linha para a evolução das vendas ao longo dos anos
sales['Calculated_Date'].value_counts().plot(kind='line', figsize=(14,6))

# Aumento de $50 na receita de cada venda
sales['Revenue'] += 50

# Quantas vendas com receita acima de $500 foram feitas por homens?
sales.loc[(sales['Customer_Gender'] == 'M') & (sales['Revenue'] == 500)].shape[0]

# Os 5 maiores valores de receita
sales.sort_values(['Revenue'], ascending=False).head(5)

# Venda com a maior receita
cond = sales['Revenue'] == sales['Revenue'].max()
sales.loc[cond]

# Média de 'Order_Quantity' para vendas com mais de $10.000 em receita
cond = sales['Revenue'] > 10_000
sales.loc[cond, 'Order_Quantity'].mean()

# Média de 'Order_Quantity' para vendas com menos de $10.000 em receita
cond = sales['Revenue'] < 10_000
sales.loc[cond, 'Order_Quantity'].mean()

# Número de vendas feitas em maio de 2016
cond = (sales['Year'] == 2016) & (sales['Month'] == 'May')
sales.loc[cond].shape[0]

# Número de vendas feitas entre maio e julho de 2016
cond = (sales['Year'] == 2016) & (sales['Month'].isin(['May', 'June', 'July']))
sales.loc[cond].shape[0]

# Box plot agrupado por mês para 'Profit' em 2016
profit_2016 = sales.loc[sales['Year'] == 2016, ['Profit', 'Month']]
profit_2016.boxplot(by='Month', figsize=(14,6))

# Adição de 7,2% de imposto sobre cada venda 'Unit_Price' nos Estados Unidos
sales.loc[sales['Country'] == 'United States', 'Unit_Price'] *= 1.072
