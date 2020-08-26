import json, operator
import random
from operator import itemgetter
from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType

userskill = "passing"
userposition = "POINT GUARD"
skillsdict = {
"scoring": "points",
"passing": "assists",
"fouling": "fouls",
}
skilltrans = skillsdict[userskill]
raw = client.players_season_totals(season_end_year=2020, output_type=OutputType.JSON)
data = json.loads(raw)
data.sort(key=operator.itemgetter(skilltrans), reverse=True)
top25 = data[:25]
output = json.dumps(top25, indent=2)
positions = json.loads(output)
result = []

for player in positions:
    if userposition in player['positions']:
        result.append(player['name'])
        continue
    else:
        continue

max = 1
if len(result) == max:
    print(result)
else:
    print(random.choice(result))
