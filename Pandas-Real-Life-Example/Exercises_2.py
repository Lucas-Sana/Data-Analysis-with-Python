#!/usr/bin/env python
# coding: utf-8

# Exercises
# The Sakila Database

# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Connecting to the Sakila database
conn = sqlite3.connect('data/sakila.db')

# Querying the database and loading data into a DataFrame
df = pd.read_sql('''
    SELECT
        rental.rental_id, rental.rental_date, rental.return_date,
        customer.last_name AS customer_lastname,
        store.store_id,
        city.city AS rental_store_city,
        film.title AS film_title, film.rental_duration AS film_rental_duration,
        film.rental_rate AS film_rental_rate, film.replacement_cost AS film_replacement_cost,
        film.rating AS film_rating
    FROM rental
    INNER JOIN customer ON rental.customer_id == customer.customer_id
    INNER JOIN inventory ON rental.inventory_id == inventory.inventory_id
    INNER JOIN store ON inventory.store_id == store.store_id
    INNER JOIN address ON store.address_id == address.address_id
    INNER JOIN city ON address.city_id == city.city_id
    INNER JOIN film ON inventory.film_id == film.film_id
    ;
''', conn, index_col='rental_id', parse_dates=['rental_date', 'return_date'])

# Display the first few rows of the DataFrame
df.head()

# What's the mean of film_rental_duration?
df['film_rental_duration'].mean()

# What's the most common rental duration?
df['film_rental_duration'].value_counts().plot(kind='bar', figsize=(14, 6))

# What is the most common rental rate?
df['film_rental_rate'].value_counts().plot(kind='pie', figsize=(6, 6))
df['film_rental_rate'].value_counts().plot(kind='bar', figsize=(14, 6))

# How is the replacement cost distributed?
df['film_replacement_cost'].plot(kind='box', vert=False, figsize=(14, 6))
ax = df['film_replacement_cost'].plot(kind='density', figsize=(14, 6))
ax.axvline(df['film_replacement_cost'].mean(), color='red')
ax.axvline(df['film_replacement_cost'].median(), color='green')

# How many films of each rating do we have?
df['film_rating'].value_counts()

# Does the film replacement cost vary depending on film rating?
df[['film_replacement_cost', 'film_rating']].boxplot(by='film_rating', figsize=(14, 6))

# Add and calculate a new rental_days column
df['rental_days'] = df[['rental_date', 'return_date']].apply(lambda x: (x[1] - x[0]).days, axis=1)
df['rental_days'].head()

# Analyze the distribution of rental_days
df['rental_days'].mean()
ax = df['rental_days'].plot(kind='density', figsize=(14, 6))
ax.axvline(df['rental_days'].mean(), color='red')

# Add and calculate a new film_daily_rental_rate column
df['film_daily_rental_rate'] = df['film_rental_rate'] / df['film_rental_duration']
df['film_daily_rental_rate'].head()

# Analyze the distribution of film_daily_rental_rate
df['film_daily_rental_rate'].mean()
ax = df['film_daily_rental_rate'].plot(kind='density', figsize=(14, 6))
ax.axvline(df['film_daily_rental_rate'].mean(), color='red')

# List 10 films with the lowest daily rental rate
df.loc[df['film_daily_rental_rate'] == df['film_daily_rental_rate'].min()].head(10)

# List 10 films with the highest daily rental rate
df.loc[df['film_daily_rental_rate'] == df['film_daily_rental_rate'].max()].head(10)

# How many rentals were made in Lethbridge city?
df.loc[df['rental_store_city'] == 'Lethbridge'].shape[0]

# How many rentals of each film rating were made in Lethbridge city?
df.loc[df['rental_store_city'] == 'Lethbridge', 'film_rating'].value_counts()
df.loc[df['rental_store_city'] == 'Lethbridge', 'film_rating'].value_counts().plot(kind='bar', figsize=(14, 6))

# How many rentals were made in Woodridge city with rental duration higher than 5 days?
df.loc[(df['rental_store_city'] == 'Woodridge') & (df['film_rental_duration'] > 5)].shape[0]

# How many rentals were made at the store with id 2 or with replacement cost lower than 10.99 USD?
df.loc[(df['store_id'] == 2) | (df['film_replacement_cost'] < 10.99)].shape[0]