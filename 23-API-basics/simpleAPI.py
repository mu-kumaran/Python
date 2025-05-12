# Using Pandas API
import pandas as pd

dict_ ={'a':[11,21,31],'b':[21,22,32]}
df = pd.DataFrame(dict_)

# print(df.head())
# print(df.mean())
# print(type(df.mean()))

# Using NBA API
from nba_api.stats.static import teams

nba_teams = teams.get_teams()

print(nba_teams[:1])

