# Using Pandas API
import pandas as pd

dict_ ={'a':[11,21,31],'b':[21,22,32]}
df = pd.DataFrame(dict_)

# print(df.head())
# print(df.mean())
# print(type(df.mean()))

# Using NBA API static
from nba_api.stats.static import teams

nba_teams = teams.get_teams()

def dict_nba(nba_teams):
    dt = {}
    temp_list = []

    for i in nba_teams[0].keys():
        for j in range(len(nba_teams)):
            temp_list.append(nba_teams[j].get(i))
        dt[i] = temp_list.copy()    
        temp_list.clear()

    del temp_list
    return dt

df_teams = pd.DataFrame(dict_nba(nba_teams))
print(df_teams.head())

df_warriors = df_teams[df_teams["nickname"]=="Warriors"]
print(df_warriors)
print(df_warriors['id'].values[0])
print(df_warriors[['id']].values[0][0])
id_warriors = df_warriors[['id']].values[0][0]

# Using nba API dynamic
from nba_api.stats.endpoints import leaguegamefinder

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)

games = gamefinder.get_data_frames()[0]   # converting from list to dataframe. list has only one element that is dataframe

# print(type(games))
print(games.head(10))

games_home = games[games['MATCHUP']=='GSW vs. HOU']
games_away = games[games['MATCHUP']=='GSW @ HOU']

print(games_home.head(10))
print(games_away.head(10))

import matplotlib.pyplot as plt

fig,ax = plt.subplots()
games_away.plot(x='GAME_DATE',y='PLUS_MINUS',ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS',ax=ax)
ax.legend(['@Houston','@homeland'])
plt.title("Golden State Warriors vs Houston Rockets")
plt.show()
