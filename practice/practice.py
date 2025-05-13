import pandas as pd
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
