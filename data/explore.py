# --- Exercise 1: Load it ---
import pandas as pd

df = pd.read_csv('data/retail_sales.csv')

# Inspection Commands
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# --- Exercise 2: Filter by region ---
south = df[df['region'] == 'South']

print(len(south))
print(south.head())

