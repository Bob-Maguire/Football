import requests, json
from Team import *
from game import *
from venues import *
from base64 import b64encode

enc = b64encode(b":MYSPORTSFEEDS").decode("ascii")

header = {'Authorization' : 'Basic %s' % enc}

#response = requests.get("https://api.mysportsfeeds.com/v2.0/pull/nfl/current/games.json", headers = header)
#response = requests.get("https://api.mysportsfeeds.com/v2.0/pull/nfl/current/player_stats_totals.json", headers = header)
#response = requests.get("https://api.mysportsfeeds.com/v2.0/pull/nfl/current/venues.json", headers = header)
#result = response.json()

#with open ('venues.txt', 'w') as out:
    #json.dump(result, out)

file = open('schedule.txt', 'r')
schedule = json.load(file)
file.close()

file = open('players.txt', 'r')
players = json.load(file)
file.close()

file = open('venues.txt', 'r')
venues = json.load(file)
file.close()

team_names = {'NYG', 'PHI', 'DAL', 'WAS', 'GB', 'CHI', 'MIN', 'DET', 'TB',
             'ATL', 'CAR', 'NO', 'SF', 'LA', 'ARI', 'SEA', 'NE', 'NYJ', 'BUF', 
             'MIA', 'JAX', 'TEN', 'IND', 'HOU', 'KC', 'OAK', 'DEN', 'LAC', 
             'BAL', 'PIT', 'CLE', 'CIN'}

teams = {}

for v in venues['venues']:
    id = v['venue']['id']
    name = v['venue']['name']
    city = v['venue']['city']
    stadium = Venues(name, id, city)
    team_id = v['homeTeam']['id']
    team_city = v['homeTeam']['city']
    team_name = v['homeTeam']['name']
    team_abbr = v['homeTeam']['abbreviation']
    teams[team_abbr] = Team(team_abbr, team_id, stadium, team_city, team_name)
    if (team_abbr == "NYG"):
        teams["NYJ"] = Team("NYJ", 51, stadium, team_city, "Jets")

game_list = []
for g in schedule['games']:
    id = g['schedule']['id']
    s_week = g['schedule']['week']
    away = g['schedule']['awayTeam']['abbreviation']
    home = g['schedule']['homeTeam']['abbreviation']
    completion = g['schedule']['playedStatus']
    awayScore = g['score']['awayScoreTotal']
    homeScore = g['score']['homeScoreTotal']

    new_game = game(id, s_week, away, home, completion, awayScore, homeScore)
    game_list.append(new_game)
    teams[new_game.away].addAwayGame(new_game)
    teams[new_game.home].addHomeGame(new_game)

#for p in players:

print(schedule['games'][0]['schedule'])
