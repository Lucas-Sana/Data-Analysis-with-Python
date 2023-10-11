import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import the numpy package under the name np
import numpy as np

# Import the pandas package under the name pd
import pandas as pd

# Import the matplotlib package under the name plt
import matplotlib.pyplot as plt

# Print the pandas version and the configuration
print(pd.__version__)

# Create an empty pandas DataFrame
pd.DataFrame(data=[None], index=[None], columns=[None])

# Create a `marvel_df` pandas DataFrame with the given marvel data
marvel_data = [ ... ]
marvel_df = pd.DataFrame(data=marvel_data)
marvel_df

# Add column names to the `marvel_df`
col_names = ['name', 'sex', 'first_appearance']
marvel_df.columns = col_names
marvel_df

# Add index names to the `marvel_df` (use the character name as index)
marvel_df.index = marvel_df['name']
marvel_df

# Drop the name column as it's now the index
marvel_df = marvel_df.drop(['name'], axis=1)
marvel_df

# Drop 'Namor' and 'Hank Pym' rows
marvel_df = marvel_df.drop(['Namor', 'Hank Pym'], axis=0)
marvel_df

# Show the first 5 elements on `marvel_df`
marvel_df.iloc[:5,]

# Show the last 5 elements on `marvel_df`
marvel_df.iloc[-5:,]

# Show just the sex of the first 5 elements on `marvel_df`
marvel_df.iloc[:5,].sex.to_frame()

# Show the first_appearance of all middle elements on `marvel_df`
marvel_df.iloc[1:-1,].first_appearance.to_frame()

# Show the first and last elements on `marvel_df`
marvel_df.iloc[[0, -1],]

# Modify the `first_appearance` of 'Vision' to year 1964
marvel_df.loc['Vision', 'first_appearance'] = 1964
marvel_df

# Add a new column to `marvel_df` called 'years_since' with the years since `first_appearance`
marvel_df['years_since'] = 2018 - marvel_df['first_appearance']
marvel_df

# Given the `marvel_df` pandas DataFrame, make a mask showing the female characters
mask = marvel_df['sex'] == 'female'
mask

# Given the `marvel_df` pandas DataFrame, get the male characters
mask = marvel_df['sex'] == 'male'
marvel_df[mask]

# Given the `marvel_df` pandas DataFrame, get the characters with `first_appearance` after 1970
mask = marvel_df['first_appearance'] > 1970
marvel_df[mask]

# Given the `marvel_df` pandas DataFrame, get the female characters with `first_appearance` after 1970
mask = (marvel_df['sex'] == 'female') & (marvel_df['first_appearance'] > 1970)
marvel_df[mask]

# Show basic statistics of `marvel_df`
marvel_df.describe()

# Given the `marvel_df` pandas DataFrame, show the mean value of `first_appearance`
marvel_df.first_appearance.mean()

# Given the `marvel_df` pandas DataFrame, show the min value of `first_appearance`
marvel_df.first_appearance.min()

# Given the `marvel_df` pandas DataFrame, get the characters with the min value of `first_appearance`
mask = marvel_df['first_appearance'] == marvel_df.first_appearance.min()
marvel_df[mask]

# Reset index names of `marvel_df`
marvel_df = marvel_df.reset_index()
marvel_df

# Plot the values of `first_appearance`
marvel_df.first_appearance.plot()

# Plot a histogram (plot.hist) with values of `first_appearance`
plt.hist(marvel_df.first_appearance)
