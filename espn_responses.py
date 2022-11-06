import os
from tabulate import tabulate
from espn_api.basketball import League
from dotenv import load_dotenv
from cleantext import clean

config = load_dotenv()

year = 2023
league_id = os.getenv('LEAGUE_ID')
espn_s2 = os.getenv('ESPN_S2')
swid = os.getenv('SWID')

league = League(league_id, year, espn_s2, swid)
top_free_agents = league.free_agents()

def get_help_menu():
    help_menu = '''
INFO: Options and description:
$fa-status     - Top 50 Free Agents and their current health
$injury-report - All players that are currently out 
$team-stats    - Win/Loss for each team
$scoreboard    - Live scoreboard
'''
    return help_menu

def get_free_agents():
    top_free_agents_and_health = []
    for player in top_free_agents:
        FA_DICT = {}
        FA_DICT['player'] = str(player.name)
        FA_DICT['health'] = str(player.injuryStatus)
        top_free_agents_and_health.append(FA_DICT)

    formatted_fa = tabulate(top_free_agents_and_health, headers='keys', tablefmt='rst')
    return formatted_fa

def get_injured_players():
    injured_players = []
    for team in league.teams:
        for player in team.roster:
            if player.injuryStatus == 'OUT' or player.injuryStatus == 'DAY_TO_DAY':
                INJURY_DICT = {}
                INJURY_DICT['player'] = str(player.name)
                INJURY_DICT['health'] = str(player.injuryStatus)
                INJURY_DICT['team'] = str(team.team_name)
                injured_players.append(INJURY_DICT)

    formatted_injured_players = tabulate(injured_players, headers='keys', tablefmt='rst')
    return formatted_injured_players

def get_win_loss():
    stats = []
    for team in league.teams:
        STATS_DICT = {}
        STATS_DICT['wins'] = str(team.wins)
        STATS_DICT['losses'] = str(team.losses)
        STATS_DICT['team'] = str(team.team_name)
        stats.append(STATS_DICT)

    formatted_stats = tabulate(stats, headers='keys', tablefmt='rst')
    return formatted_stats

def get_score_board():
    scoreboard = []
    index = 0
    matchups = league.scoreboard()
    for matchup in matchups:
        SB_DICT = {}
        SB_DICT['home team'] = clean(str(matchup.home_team.team_name), no_emoji=True, lower=False)
        SB_DICT['home points'] = str(matchup.home_final_score)
        SB_DICT['away points'] = str(matchup.away_final_score)
        SB_DICT['away team'] = clean(str(matchup.away_team.team_name), no_emoji=True, lower=False)
        scoreboard.append(SB_DICT)
        index += 1
    formatted_scoreboard = tabulate(scoreboard, headers='keys', tablefmt='fancy_grid', numalign='center', stralign='left')
    return formatted_scoreboard
