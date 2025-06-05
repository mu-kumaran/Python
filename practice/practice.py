import pandas as pd

df = pd.read_csv("new_songs.csv")
df1 = pd.read_excel("sales.xlsx")
# print(df1.head())

songs = {
    'Artist':['MJ','Pink Floyd','Meat Loaf','AC/DC','Eagels'],
    'Album':['Thriller','Back in Black','Darkside of the Moon','The BodyGuard','Bat Out of Hell'],
    'Released':[1982,1980,1973,1992,1977],
    'Genre':['Pop','Rock','Metal','Light','Disco'],
    'Length':['10 mins','20 mins','5 mins','8 mins','12 mins']
    }

df2 = pd.DataFrame(songs)
print(df2)

new = df2[["Length"]]
# print(new)

new1 = df2[['Length','Genre','Artist']]
# print(new1)

new2 = df2['Length']
# print(new2)

s = df2['Length'].unique()
print(s)

t1 = df2[['Released']]>1980
print(t1)

t = df2[df2['Released']>1980]
print(t)