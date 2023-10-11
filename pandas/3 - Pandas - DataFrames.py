import numpy as np
import pandas as pd

df = pd.DataFrame({
    'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
    'GDP': [
        1785387,
        2833687,
        3874437,
        2167744,
        4602367,
        2950039,
        17348075
    ],
    'Surface Area': [
        9984670,
        640679,
        357114,
        301336,
        377930,
        242495,
        9525067
    ],
    'HDI': [
        0.913,
        0.888,
        0.916,
        0.873,
        0.891,
        0.907,
        0.915
    ],
    'Continent': [
        'America',
        'Europe',
        'Europe',
        'Europe',
        'Asia',
        'Europe',
        'America'
    ]
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])

df.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]

# The next few cells include operations like checking the columns, indexes, and basic statistics.

df.columns

df.index

df.info()

df.size

df.shape

df.describe()

df.dtypes

df.dtypes.value_counts()

# Indexing, Selection, and Slicing

df.loc['Canada']

df.iloc[-1]

df['Population']

df['Population'].to_frame()

df[['Population', 'GDP']]

df[1:3]

df.loc['France': 'Italy']

df.loc['France': 'Italy', 'Population']

df.loc['France': 'Italy', ['Population', 'GDP']]

df.iloc[0]

df.iloc[-1]

df.iloc[[0, 1, -1]]

df.iloc[1:3]

df.iloc[1:3, 3]

df.iloc[1:3, [0, 3]]

df.iloc[1:3, 1:3]

# Conditional selection (boolean arrays)

df['Population'] > 70

df.loc[df['Population'] > 70]

df.loc[df['Population'] > 70, 'Population']

df.loc[df['Population'] > 70, ['Population', 'GDP']]

# Dropping stuff

df.drop('Canada')

df.drop(['Canada', 'Japan'])

df.drop(columns=['Population', 'HDI'])

df.drop(['Italy', 'Canada'], axis=0)

df.drop(['Population', 'HDI'], axis=1)

df.drop(['Population', 'HDI'], axis=1)

df.drop(['Population', 'HDI'], axis='columns')

df.drop(['Canada', 'Germany'], axis='rows')

# Operations

df[['Population', 'GDP']] / 100

crisis = pd.Series([-1_000_000, -0.3], index=['GDP', 'HDI'])
crisis

df[['GDP', 'HDI']] + crisis

# Modifying DataFrames

langs = pd.Series(
    ['French', 'German', 'Italian'],
    index=['France', 'Germany', 'Italy'],
    name='Language'
)

langs

df['Language'] = langs

df['Language'] = 'English'

df.rename(
    columns={
        'HDI': 'Human Development Index',
        'Anual Popcorn Consumption': 'APC'
    }, index={
        'United States': 'USA',
        'United Kingdom': 'UK',
        'Argentina': 'AR'
    })

df.rename(index=str.upper)

df.rename(index=lambda x: x.lower())

df.drop(columns='Language', inplace=True)

df.loc['China'] = pd.Series({'Population': 1_400_000_000, 'Continent': 'Asia'})

df.drop('China', inplace=True)

# More radical index changes

df.reset_index()

df.set_index('Population')

# Creating columns from other columns

df[['Population', 'GDP']]

df['GDP'] / df['Population']

df['GDP Per Capita'] = df['GDP'] / df['Population']

df.describe()

population = df['Population']

population.min(), population.max()

population.sum()

population.sum() / len(population)

population.mean()

population.std()

population.median()

population.describe()

population.quantile(.25)

population.quantile([.2, .4, .6, .8, 1])