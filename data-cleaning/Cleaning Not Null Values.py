# Cleaning not-null values
# After dealing with many datasets I can tell you that "missing data" is not such a big deal. The best thing that can happen is to clearly see values like `np.nan`. The only thing you need to do is just use methods like `isnull` and `fillna`/`dropna` and pandas will take care of the rest.
# But sometimes, you can have invalid values that are not just "missing data" (`None`, or `nan`). For example:

import numpy as np
import pandas as pd

df = pd.DataFrame({
    'Sex': ['M', 'F', 'F', 'D', '?'],
    'Age': [29, 30, 24, 290, 25],
})
df


# The previous `DataFrame` doesn't have any "missing value", but clearly has invalid data. `290` doesn't seem like a valid age, and `D` and `?` don't correspond with any known sex category. How can you clean these not-missing, but clearly invalid values then?
# Finding Unique Values 
# The first step to clean invalid values is to **notice** them, then **identify** them and finally handle them appropriately (remove them, replace them, etc). Usually, for a "categorical" type of field (like Sex, which only takes values of a discrete set `('M', 'F')`), we start by analyzing the variety of values present. For that, we use the `unique()` method:

df['Sex'].unique()

df['Sex'].value_counts()


# Clearly if you see values like `'D'` or `'?'`, it'll immediately raise your attention. Now, what to do with them? Let's say you picked up the phone, called the survey company and they told you that `'D'` was a typo and it should actually be `F`. You can use the `replace` function to replace these values:

df['Sex'].replace('D', 'F')

# It can accept a dictionary of values to replace. For example, they also told you that there might be a few `'N's`, that should actually be `'M's`:

df['Sex'].replace({'D': 'F', 'N': 'M'})

# If you have many columns to replace, you could apply it at "DataFrame level":

df.replace({
    'Sex': {
        'D': 'F',
        'N': 'M'
    },
    'Age': {
        290: 29
    }
})

# In the previous example, I explicitly replaced 290 with 29 (assuming it was just an extra 0 entered at data-entry phase). But what if you'd like to remove all the extra 0s from the ages columns? (example, `150 > 15`, `490 > 49`).
# The first step would be to just set the limit of the "not possible" age. Is it 100? 120? Let's say that anything above 100 isn't credible for **our** dataset. We can then combine boolean selection with the operation:

df[df['Age'] > 100]

# And we can now just divide by 10:

df.loc[df['Age'] > 100, 'Age'] = df.loc[df['Age'] > 100, 'Age'] / 10

print(df)

# Duplicates
# Checking duplicate values is extremely simple. It'll behave differently between Series and DataFrames. Let's start with Series. As an example, let's say we're throwing a fancy party and we're inviting Ambassadors from Europe. But can only invite one ambassador per country. This is our original list, and as you can see, both the UK and Germany have duplicated ambassadors:

ambassadors = pd.Series([
    'France',
    'United Kingdom',
    'United Kingdom',
    'Italy',
    'Germany',
    'Germany',
    'Germany',
], index=[
    'Gérard Araud',
    'Kim Darroch',
    'Peter Westmacott',
    'Armando Varricchio',
    'Peter Wittig',
    'Peter Ammon',
    'Klaus Scharioth '
])

print(ambassadors)

# The two most important methods to deal with duplicates are `duplicated` (that will tell you which values are duplicates) and `drop_duplicates` (which will just get rid of duplicates):

ambassadors.duplicated()

# In this case `duplicated` didn't consider `'Kim Darroch'`, the first instance of the United Kingdom or `'Peter Wittig'` as duplicates. That's because, by default, it'll consider the first occurrence of the value as not-duplicate. You can change this behavior with the `keep` parameter:

ambassadors.duplicated(keep='last')

# In this case, the result is "flipped", `'Kim Darroch'` and `'Peter Wittig'` (the first ambassadors of their countries) are considered duplicates, but `'Peter Westmacott'` and `'Klaus Scharioth'` are not duplicates. You can also choose to mark all of them as duplicates with `keep=False`:

ambassadors.duplicated(keep=False)

# A similar method is `drop_duplicates`, which just excludes the duplicated values and also accepts the `keep` parameter:

ambassadors.drop_duplicates()

ambassadors.drop_duplicates(keep='last')

ambassadors.drop_duplicates(keep=False)

# Duplicates in DataFrames
# Conceptually speaking, duplicates in a DataFrame happen at "row" level. Two rows with exactly the same values are considered to be duplicates:

players = pd.DataFrame({
    'Name': [
        'Kobe Bryant',
        'LeBron James',
        'Kobe Bryant',
        'Carmelo Anthony',
        'Kobe Bryant',
    ],
    'Pos': [
        'SG',
        'SF',
        'SG',
        'SF',
        'SF'
    ]
})

print(players)

# In the previous DataFrame, we clearly see that Kobe is duplicated; but he appears with two different positions. What does `duplicated` say?

players.duplicated()

# Again, conceptually, "duplicated" means "all the column values should be duplicates". We can customize this with the `subset` parameter:

players.duplicated(subset=['Name'])

# And the same rules of `keep` still apply:

players.duplicated(subset=['Name'], keep='last')

# `drop_duplicates` takes the same parameters:

players.drop_duplicates()

players.drop_duplicates(subset=['Name'])

players.drop_duplicates(subset=['Name'], keep='last')

# Text Handling
# Cleaning text values can be incredibly hard. Invalid text values involves, 99% of the time, mistyping, which is completely unpredictable and doesn't follow any pattern. Thankfully, it's not so common these days, where data-entry tasks have been replaced by machines. Still, let's explore the most common cases:
# Splitting Columns
# The result of a survey is loaded and this is what you get:

df = pd.DataFrame({
    'Data': [
        '1987_M_US _1',
        '1990?_M_UK_1',
        '1992_F_US_2',
        '1970?_M_   IT_1',
        '1985_F_I  T_2'
]})

print(df)

# You know that the single columns represent the values "year, Sex, Country and number of children", but it's all been grouped in the same column and separated by an underscore. Pandas has a convenient method named `split` that we can use in these situations:

df['Data'].str.split('_')

df['Data'].str.split('_', expand=True)

df = df['Data'].str.split('_', expand=True)

df.columns = ['Year', 'Sex', 'Country', 'No Children']

# You can also check which columns contain a given value with the `contains` method:

print(df)

df['Year'].str.contains('\?')

df['Country'].str.contains('U')

# Removing blank spaces (like in `'US '` or `'I  T'` can be achieved with `strip` (`lstrip` and `rstrip` also exist) or just `replace`:

df['Country'].str.strip()

df['Country'].str.replace(' ', '')

# As we said, `replace` and `contains` take regex patterns, which can make it easier to replace values in bulk:

df['Year'].str.replace(r'(?P<year>\d{4})\?', lambda m: m.group('year'))


# But, be warned:
# > Some people, when confronted with a problem, think "I know, I'll use regular expressions." Now they have two problems.
# As you can see, all these string/text-related operations are applied over the `str` attribute of the series. That's because they have a special place in Series handling and you can read more about it [here](https://pandas.pydata.org/pandas-docs/stable/text.html).