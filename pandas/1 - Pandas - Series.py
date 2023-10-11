import pandas as pd
import numpy as np

# Pandas Series

# In millions
g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])

# Someone might not know we're representing population in millions of inhabitants. Series can have a `name`, to better document the purpose of the Series:
g7_pop.name = 'G7 Population in millions'

# Series are pretty similar to numpy arrays:

g7_pop.dtype

g7_pop.values

# They're actually backed by numpy arrays:

type(g7_pop.values)

# And they _look_ like simple Python lists or Numpy Arrays. But they're actually more similar to Python `dict`s.
# A Series has an `index`, that's similar to the automatic index assigned to Python's lists:

g7_pop[0]

g7_pop[1]

g7_pop.index

# But, in contrast to lists, we can explicitly define the index:

g7_pop.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]

# Compare it with the following table: 
# We can say that Series look like "ordered dictionaries". We can actually create Series out of dictionaries:

pd.Series({
    'Canada': 35.467,
    'France': 63.951,
    'Germany': 80.94,
    'Italy': 60.665,
    'Japan': 127.061,
    'United Kingdom': 64.511,
    'United States': 318.523
}, name='G7 Population in millions')

pd.Series(
    [35.467, 63.951, 80.94, 60.665, 127.061, 64.511, 318.523],
    index=['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom',
       'United States'],
    name='G7 Population in millions')

pd.Series(g7_pop, index=['France', 'Germany', 'Italy', 'Spain'])

# Indexing

g7_pop['Canada']

g7_pop['Japan']

g7_pop.iloc[0]

g7_pop.iloc[-1]

g7_pop[['Italy', 'France']]

g7_pop.iloc[[0, 1]]

g7_pop['Canada': 'Italy']

# Conditional selection (boolean arrays)

g7_pop > 70

g7_pop[g7_pop > 70]

g7_pop.mean()

g7_pop[g7_pop > g7_pop.mean()]

g7_pop[(g7_pop > g7_pop.mean() - g7_pop.std() / 2) | (g7_pop > g7_pop.mean() + g7_pop.std() / 2)]

# Operations and methods

g7_pop * 1_000_000

g7_pop.mean()

np.log(g7_pop)

g7_pop['France': 'Italy'].mean()

# Boolean arrays (Work in the same way as numpy)

g7_pop > 80

g7_pop[g7_pop > 80]

g7_pop[(g7_pop > 80) | (g7_pop < 40)]

g7_pop[(g7_pop > 80) & (g7_pop < 200)]

# Modifying series

g7_pop['Canada'] = 40.5

g7_pop.iloc[-1] = 500

g7_pop[g7_pop < 70]

g7_pop[g7_pop < 70] = 99.99
