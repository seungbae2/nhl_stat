import json

def summary():
	with open('static/data/kingsVSbluejackets.json', 'r') as file:
	    data = file.read()

	summary_data = json.loads(data)
	
	away_data = summary_data['liveData']['boxscore']['teams']['away']['teamStats']['teamSkaterStats']
	home_data = summary_data['liveData']['boxscore']['teams']['home']['teamStats']['teamSkaterStats']
	
	game_date = summary_data["gameData"]["datetime"]["dateTime"]
	home_team = summary_data["gameData"]["teams"]["home"]["name"]
	away_team = summary_data["gameData"]["teams"]["away"]["name"]

	game_date = game_date.split("T")[0]

	stat_data = {
		'game_date':game_date,
		'home_team':home_team,
		'away_team':away_team,
		'home_data':home_data,
		'away_data':away_data
	}

	with open('static/data/game_stat.json', 'w') as output:
		json.dump(stat_data, output)

	return stat_data

def event():

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
	            x = play['coordinates']['x']+100
	            y = play['coordinates']['y']+50
	            #print(play['coordinates']['x'])
	            #print(play['coordinates']['y'])


	        if bool(play['team']):
	            team_name = play['team']['name']
	            #print(play['team']['name'])
	            
	        period = play['about']['period']
        	description = play['result']['description']
	        
	        data = {
	            'event': event,
	            'x': x,
	            'y': y,
	            'name': team_name,
	            'game_date': game_date,
	            'home_team': home_team,
	            'away_team': away_team,
	            'period': period,
	            'description': description
	        }
	        #print(data)
	        nhl_data.append(data)
		
	with open('static/data/result.json', 'w') as output:
		json.dump(nhl_data, output)


	return nhl_data
