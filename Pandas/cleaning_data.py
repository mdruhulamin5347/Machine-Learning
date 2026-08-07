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

# df = pd.read_csv("RadioLens.csv")
# # df = df.dropna()


# x = df["Age"].mean()
# y = df["Age"].median()
# z = df["Age"].mode()[0]
# df = df.fillna({"age": x}, inplace = True)

# print(df.to_string())







# Data of Wrong Format 

# df = pd.read_csv('RadioLens.csv')

# df['Arrival Time'] = pd.to_datetime(df['Arrival Time'], format='mixed')

# df.dropna(subset=['Arrival Time'], inplace = True)

# print(df.to_string())






# Pandas - Fixing Wrong Data

# df = pd.read_csv('RadioLens.csv')

# df.loc[4,'Age'] = 47

# print(df.to_string())


# for x in df.index:
#   if df.loc[x, "Age"] > 90:
#     df.loc[x, "Age"] = 90

# print(df.to_string())


# for x in df.index:
#   if df.loc[x, "Age"] > 120:
#     df.drop(x, inplace = True)
    
    
    





# Pandas - Removing Duplicates


df = pd.read_csv('RadioLens.csv')
print(df.duplicated())
df = df.drop_duplicates()
print(df.to_string())