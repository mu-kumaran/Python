import pandas as pd

df = pd.read_excel("sales.xlsx")
print(df)

new_index = ['a','b','c','d','e']

df.index = new_index

print(df)