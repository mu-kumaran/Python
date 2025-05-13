import pandas as pd

df = pd.read_excel("sales.xlsx")
print(df)

new_index = ['a','b','c','d','e']

df.index = new_index

print(df)

# Converting nested list and dictionary to a dataframe

lst1 = [{1:'A',2:'B',3:'C'},{1:'a',2:'b',3:'c'}]

dt = {}
temp_list = []
lst =[]

for i in lst1[0].keys():
    for j in range(len(lst1)):
        temp_list.append(lst1[j].get(i))
    lst.append(temp_list.copy())
    dt[i] = temp_list.copy()    
    temp_list.clear()

del temp_list
print(lst)  # [['A','a'],['B','b'],['C','c']]
print(dt)   # {1: ['A', 'a'], 2: ['B', 'b'], 3: ['C', 'c']}

df = pd.DataFrame(dt)
print(df.head())