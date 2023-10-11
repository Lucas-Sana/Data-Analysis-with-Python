import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading external data & Plotting
# Source: https://blockchain.info/charts/market-price

df = pd.read_csv('data/btc-market-price.csv', header=None)
df.columns = ['Timestamp', 'Price']
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)

print(df.head())

# Putting everything together
df = pd.read_csv(
    'data/btc-market-price.csv',
    header=None,
    names=['Timestamp', 'Price'],
    index_col=0,
    parse_dates=True
)

print(df.head())

# Plotting basics
df.plot(figsize=(16, 9), title='Bitcoin Price 2017-2018')

# A more challenging parsing
eth = pd.read_csv('data/eth-price.csv', parse_dates=True, index_col=0)

prices = pd.DataFrame(index=df.index)
prices['Bitcoin'] = df['Price']
prices['Ether'] = eth['Value']

prices.plot(figsize=(12, 6))
prices.loc['2017-12-01':'2018-01-01'].plot(figsize=(12, 6))
