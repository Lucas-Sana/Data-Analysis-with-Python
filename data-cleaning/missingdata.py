import numpy as np
import pandas as pd

# What does "missing data" mean? What is a missing value? 
# It depends on the origin of the data and the context it was generated.
# For example, for a survey, a _`Salary`_ field with an empty value, or a number 0, or an invalid value (a string for example) can be considered "missing data".
# These concepts are related to the values that Python will consider "Falsy":

falsy_values = (0, False, None, '', [], {})

# For Python, all the values above are considered "falsy":

any(falsy_values)

# Numpy has a special "nullable" value for numbers which is np.nan. It's _NaN_: "Not a number"

np.nan

# The np.nan value is kind of a virus. Everything that it touches becomes `np.nan`:

3 + np.nan
a = np.array([1, 2, 3, np.nan, np.nan, 4])
a.sum()
a.mean()

# This is better than regular None values, which in the previous examples would have raised an exception:

3 + None

# For a numeric array, the `None` value is replaced by `np.nan`:

a = np.array([1, 2, 3, np.nan, None, 4], dtype='float')
a

# As we said, np.nan is like a virus. If you have any nan value in an array and you try to perform an operation on it, you'll get unexpected results:

a = np.array([1, 2, 3, np.nan, np.nan, 4])
a.mean()
a.sum()

# Numpy also supports an "Infinite" type:

np.inf

# Which also behaves as a virus:

3 + np.inf
np.inf / 3
np.inf / np.inf
b = np.array([1, 2, 3, np.inf, np.nan, 4], dtype=np.float)
b.sum()


# Checking for `nan` or `inf`
# There are two functions: `np.isnan` and `np.isinf` that will perform the desired checks:

np.isnan(np.nan)
np.isinf(np.inf)

# And the joint operation can be performed with `np.isfinite`.

np.isfinite(np.nan), np.isfinite(np.inf)

# np.isnan and np.isinf also take arrays as inputs, and return boolean arrays as results:

np.isnan(np.array([1, 2, 3, np.nan, np.inf, 4]))
np.isinf(np.array([1, 2, 3, np.nan, np.inf, 4]))
np.isfinite(np.array([1, 2, 3, np.nan, np.inf, 4]))

# Note: It's not so common to find infinite values. From now on, we'll keep working with only np.nan


# Filtering them out
# Whenever you're trying to perform an operation with a Numpy array and you know there might be missing values, 
# you'll need to filter them out before proceeding, 
# to avoid nan propagation. We'll use a combination of the previous np.isnan + boolean arrays for this purpose:

a = np.array([1, 2, 3, np.nan, np.nan, 4])
a[~np.isnan(a)]

# Which is equivalent to:

a[np.isfinite(a)]

# And with that result, all the operation can be now performed:

a[np.isfinite(a)].sum()
a[np.isfinite(a)].mean()