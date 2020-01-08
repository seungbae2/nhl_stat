import json


def scrape():

	with open('static/data/kingsVSbluejackets.json', 'r') as file:
	    data = file.read()

	obj = json.loads(data)

	allPlays = obj["liveData"]["plays"]['allPlays']

	game_date = obj["gameData"]["datetime"]["dateTime"]
	home_team = obj["gameData"]["teams"]["home"]["name"]
	away_team = obj["gameData"]["teams"]["away"]["name"]

	game_date = game_date.split("T")[0]

	nhl_data = []


	for play in allPlays:
    
	    if 'team' in play.keys():
	        #print(play.keys())
	        event = play['result']['event']
	        #print(play['result']['event'])

	        if bool(play['coordinates']):
	            x = play['coordinates']['x']
	            y = play['coordinates']['y']
	            #print(play['coordinates']['x'])
	            #print(play['coordinates']['y'])


	        if bool(play['team']):
	            team_name = play['team']['name']
	            #print(play['team']['name'])
	            
	        
	        data = {
	            'event': event,
	            'x': x,
	            'y': y,
	            'name': team_name,
	            'game_date': game_date,
	            'home_team': home_team,
	            'away_team': away_team
        	}
	        #print(data)
	        nhl_data.append(data)
		
	with open('static/data/result.json', 'w') as output:
		json.dump(nhl_data, output)


	return nhl_data
