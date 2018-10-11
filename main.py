import requests, json
from base64 import b64encode

enc = b64encode(b"").decode("ascii")

header = {'Authorization' : 'Basic %s' % enc}

#response = requests.get("https://api.mysportsfeeds.com/v1.0/pull/nfl/current/full_game_schedule.json", headers = header)
#result = response.json()

#with open ('schedule.txt', 'w') as out:
#    json.dump(result, out)

file = open('schedule.txt', 'r')
result = json.load(file)
file.close()

print(result)