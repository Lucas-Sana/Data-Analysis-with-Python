import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Let's get started by importing Bitcoin and Ether data:
df = pd.read_csv('data/btc-eth-prices-outliers.csv', index_col=0, parse_dates=True)
df.head()

# And now we can run a simple visualization:
df.plot(figsize=(16, 9))

# There are clearly some invalid values, both ETH and BTC have huge spikes. On top of that, there seems to be some data missing in Ether between December 2017 and and January 2018:
df.loc['2017-12': '2017-12-15'].plot(y='Ether', figsize=(16, 9))

df_na = df.loc['2017-12': '2017-12-15']

# Are those null values?
df_na['Ether'].isna().values.any()

# When? what periods of time?
df_na.loc[df_na['Ether'].isna()]

# Let's add a little bit more context:
df.loc['2017-12-06': '2017-12-12']

# We now need to decide what we'll do with the missing values. Drop them? fill them? If we decide to fill them, what will be use as fill value? For example: we can use the previous value and just assume the price stayed the same.
df.loc['2017-12-06': '2017-12-12'].fillna(method='bfill')

df.fillna(method='bfill', inplace=True)

# Let's take a look now:
df.plot(figsize=(16, 9))

# Much better. We now need to fix the huge spikes. The first step is identifying them. How can we do it? The simple answer is of course visually. They seem to be located in the last 10 days of Dec 2017 and first of March 2018:
df['2017-12-25':'2018-01-01'].plot()
df['2018-03-01': '2018-03-09'].plot()

# Apparently, they're located in '2017-12-28' and '2018-03-04':
df_cleaned = df.drop(pd.to_datetime(['2017-12-28', '2018-03-04']))
df_cleaned.plot(figsize=(16, 9))

# Now it looks much better. Our data seems to be clean.
# Cleaning Analysis 
# Visualizations helps make sense of the data and let us judge if our analysis and work is on the right track. But we need a more powerful method to handle our data. That's what we call "analysis". We'll use analytical methods to identify these outliers or these skewed values.
# Central Tendency 
# We'll use a set of common indicators of to measure central tendency and identify these outliers:
# mean
# The mean is probably the most common and popular one. The problem is that it's really sensitive to outliers. The mean of our dataset with invalid values is:
df.mean()
# Both values seem too high. That's because the outliers are skewing with the mean:
df_cleaned.mean()

# median
df.median()

# mode
# It doesn't make much sense to measure the mode, as we have continuous values. But you can do it just with `df.mode()`.
# Visualizing distribution
# Now we can use a few of the charts that we saw before + seaborn to visualize the distribution of our values. In particular, we're interested in **histograms**:
df_cleaned.plot(kind='hist', y='Ether', bins=150)
df_cleaned.plot(kind='hist', y='Bitcoin', bins=150)

# Using seaborn:
fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Ether'], ax=ax)

fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], rug=True, ax=ax)

# Seaborn's `distplot` is a general method that will plot a histogram, a KDE and a rugplot. You can also use them as separate:
fig, ax = plt.subplots(figsize=(15, 7))
sns.kdeplot(df_cleaned['Ether'], shade=True, cut=0, ax=ax)
sns.rugplot(df_cleaned['Ether'], ax=ax);

# We can also visualize a cumulative plot of our distribution:
fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))

# This plot shows how many samples fall behind a certain value. We can increase the number of bins in order to have more detail:
fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax, bins=50,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))

# Visualizing bivariate distributions
# The most common way to observe a bivariate distribution is a scatterplot, the `jointplot` will also include the distribution of the variables:
sns.jointplot(x="Bitcoin", y="Ether", data=df_cleaned, size=9)

# If you want only a scatter plot, you can use the `regplot` method, that also fits a linear regression model in the plot:
fig, ax = plt.subplots(figsize=(15, 7))
sns.regplot(x="Bitcoin", y="Ether", data=df_cleaned, ax=ax)

# Quantiles, quartiles and percentiles
df_cleaned['Bitcoin'].quantile(.2)

fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax, bins=50,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
ax.axhline(0.2, color='red')
ax.axvline(df_cleaned['Bitcoin'].quantile(.2), color='red')

df_cleaned['Bitcoin'].quantile(.5)

df_cleaned['Bitcoin'].median()

fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax, bins=50,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
ax.axhline(0.5, color='red')
ax.axvline(df_cleaned['Bitcoin'].quantile(.5), color='red')

fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax, bins=50,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
ax.axhline(0.5, color='red')
ax.axvline(df_cleaned['Bitcoin'].median(), color='red')

# Quantile `0.25` == Percentile `25%` == Quartile `1st`
# Dispersion
# We'll use a few methods to measure dispersion in our dataset, most of them well known:
# * Range
# * Variance and Standard Deviation
# * IQR
# Range
# Range is fairly simple to understand, it's just the max - min values:
df['Bitcoin'].max() - df['Bitcoin'].min()

# Range is **really** sensitive to outliers. As you can see, the range value is extremely high (might indicate the presence of outliers / invalid values).
df_cleaned['Bitcoin'].max() - df_cleaned['Bitcoin'].min()

# This value now makes a lot more sense. We know that Bitcoin had a high in about 20k, and it was around 900 when we started measuring. It makes more sense now.
# Variance and Standard Deviation
df['Bitcoin'].var()
df['Bitcoin'].std()

# Both variance and std are sensible to outliers as well. We can check with our cleaned dataset:
df_cleaned['Bitcoin'].std()

# ### IQR
# The [Interquartile range](https://en.wikipedia.org/wiki/Interquartile_range) is a good measure of "centered" dispersion, and is calculated as `Q3 - Q1` (3rd quartile - 1st quartile).
df['Bitcoin'].quantile(.75) - df['Bitcoin'].quantile(.25)
df_cleaned['Bitcoin'].quantile(.75) - df_cleaned['Bitcoin'].quantile(.25)

# As you can see, IQR is more robust than std or range, because it's not so sensitive to outliers.
# Analytical Analysis of invalid values
# We can now use the measurements we've seen to analyze those values that seem invalid.
# Using `std`: Z scores
# We can now define those values that are a couple of Z scores above or below the mean (or the max/min value). Example:
upper_limit = df['Bitcoin'].mean() + 2 * df['Bitcoin'].std()
lower_limit = df['Bitcoin'].mean() - 2 * df['Bitcoin'].std()

print("Upper Limit: {}".format(upper_limit))
print("Lower Limit: {}".format(lower_limit))

fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df['Bitcoin'], ax=ax)
ax.axvline(lower_limit, color='red')
ax.axvline(upper_limit, color='red')

# Seems like this is a good measurement. Our lower limit doesn't make a lot of sense, as negative values are invalid. But our upper limit has a really good measure. Anything above \$27,369 is considered to be an invalid value. Pretty accurate.
# Using IQRs
# We can use the IQR instead of std if we think that the standard deviation might be **too** affected by the outliers/invalid values.
iqr = df['Bitcoin'].quantile(.75) - df['Bitcoin'].quantile(.25)
print(iqr)

upper_limit = df['Bitcoin'].mean() + 2 * iqr
lower_limit = df['Bitcoin'].mean() - 2 * iqr

print("Upper Limit: {}".format(upper_limit))
print("Lower Limit: {}".format(lower_limit))

fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df['Bitcoin'], ax=ax)
ax.axvline(lower_limit, color='red')
ax.axvline(upper_limit, color='red')

# Our measurement now is a little bit less precise. There are a few valid values (20k) that seem to be above our upper limit. Regardless, it's still a good indicator.
# Cleaning invalid values analytically
# It's time now to remove these invalid values analytically, we'll use the upper limit defined by standard deviation:
upper_limit = df['Bitcoin'].mean() + 2 * df['Bitcoin'].std()
df[df['Bitcoin'] < upper_limit].plot(figsize=(16, 7))
df.drop(df[df['Bitcoin'] > upper_limit].index).plot(figsize=(16, 7))
