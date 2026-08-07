import pandas as pd



#Pandas Series

# series = [2,3,5,6]
# print(pd.Series(series))

# series2 = [4,5,6,6]
# pd_series2 = pd.Series(series2, index=['a','b','c','d'])
# print(pd_series2["b"])



# key_value = {"motherboard":20500,"processor":22000,"ram":28400}
# pd_key_value = pd.Series(key_value)
# print(pd_key_value)








# Pandas DataFrame

# my_data = {
#     "product": [
#         "Motherboard",
#         "Processor",
#         "RAM",
#         "HDD",
#         "Power Supplier"
#     ],
#     "price" : [
#         "20500",
#         "22000",
#         "28400",
#         "14000",
#         "12999"
#     ]
# }

# results = pd.DataFrame(my_data,index=["a","b","c","d","e"])
# # print(results)
# print(results.loc["a"])







# Pandas Read CSV

# print(pd.options.display.max_rows)

# pd.options.display.max_rows = 9999

# df = pd.read_csv('RadioLens.csv')
# print(df)









# Pandas Read JSON

df = pd.read_json('json_data.json')
print(df.to_string()) 





# Pandas - Analyzing DataFrames

