"""
Data cleaning means fixing bad data in your data set.

Bad data could be:

Empty cells
Data in wrong format
Wrong data
Duplicates

"""

import pandas  as pd

# Empty Cells

df = pd.read_csv("RadioLens.csv")
# df = df.dropna()


x = df["Age"].mean()
y = df["Age"].median()
z = df["Age"].mode()[0]
df = df.fillna({"age": x}, inplace = True)

print(df.to_string())
