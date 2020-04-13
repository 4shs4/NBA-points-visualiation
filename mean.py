import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.static import teams
import numpy as np
from nba_api.stats.endpoints import leaguegamefinder


nba_teams_df = pd.DataFrame(teams.get_teams())
teams_abbreviation_list = nba_teams_df['abbreviation'].tolist()


def get_team_id(x):
    team_df = nba_teams_df[nba_teams_df['abbreviation'] == x]
    team_id = team_df.iloc[0][0]
    return team_id

number_of_games = 100
compared_team_abb = "LAL"
for abb in teams_abbreviation_list:
    if(abb == compared_team_abb):
        continue
    first_team_id = get_team_id(compared_team_abb)
    second_team_id = get_team_id(abb)

    first_team_games_df = leaguegamefinder.LeagueGameFinder(
        team_id_nullable=first_team_id).get_data_frames()[0].head(number_of_games)
    second_team_games_df = leaguegamefinder.LeagueGameFinder(
        team_id_nullable=second_team_id).get_data_frames()[0].head(number_of_games)
    fig, ax = plt.subplots()
    first_team_games_df.plot(x='GAME_DATE', y='PTS', ax=ax)
    second_team_games_df.plot(x='GAME_DATE', y='PTS', ax=ax)
    ax.legend([compared_team_abb, abb])
    imgName = (compared_team_abb+'vs'+abb+'.png')
    plt.savefig(imgName)
    plt.close(fig)
    print('done')

