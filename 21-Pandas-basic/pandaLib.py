import pandas as pd

# importing .CSV file
csv_path = "births-deaths-by-region.csv"
df = pd.read_csv(csv_path) 
# print(df.head(10))

# importing .xlsx file
excel_path = "salesData.xlsx"
df1 = pd.read_excel(excel_path)
# print(df1)
# print(df1.head())

# creating dataframe
songs = {
    'Artist':['MJ','Pink Floyd','Meat Loaf','AC/DC','Eagels'],
    'Album':['Thriller','Back in Black','Darkside of the Moon','The BodyGuard','Bat Out of Hell'],
    'Released':[1982,1980,1973,1992,1977],
    'Genre':['Pop','Rock','Metal','Light','Disco'],
    'Length':['10 mins','20 mins','5 mins','8 mins','12 mins']
}

df2 = pd.DataFrame(songs)
# print(df2)
print(df2.head()) # display first 5 rows in general
# print(df2.head(3)) # display first 3 rows

x = df2[['Length']]
y = df2[['Artist','Genre','Length']]
z = df2['Length']
print(x)
# print(y)
print(z)
print(type(x),type(z))

a = df2.iloc[0,1]
b= df2.iloc[1,2]
c = df2.loc[0,'Artist']
d = df2.loc[2,'Album']
# print(a,b,c,d)

# Slicing dataframes

s = df2.iloc[0:2,0:3]
# print(s)
t = df2.loc[0:3,'Album':'Genre']
# print(t)

# unique() method
u= df['Period'].unique()
# print(u)

# Using conditions inequality operators to list out elements
s1 = df2['Released']>=1980   #returns a bool value - True or False
# print(s1)

df3 = df2[df2['Released']>=1980]
# print(df3)

#Export to CSV file
df3.to_csv('new_songs.csv')

df4 = pd.read_csv('new_songs.csv')
# print(df4)

# Changing the index of the dataframe using index attribute

df = pd.read_excel("sales.xlsx")
print(df)

new_index = ['a','b','c','d','e']

df.index = new_index

print(df)
