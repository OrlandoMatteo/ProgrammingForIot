def get_players(file_content):
	return file_content['players']

def average_heigth(file_content):
	players=get_players(file_content)
	heigths=[p['hgt']/39.37 for p in players]
	return sum(heigths)/len(heigths)

def average_weigth(file_content):
	players=get_players(file_content)
	weigths=[p['weight']/2.205 for p in players]
	return sum(weigths)/len(weigths)

def average_ratings(file_content):
	players=get_players(file_content)
	num_players=len(players)
	avg_ratings=dict.fromkeys(players[0]['ratings'][0],0)
	for player in players:
		player_ratings=player['ratings'][0]
		for key in player_ratings.keys():
			avg_ratings[key]+=player_ratings[key]/num_players
	return avg_ratings
			
def average_age(file_content):
	players=get_players(file_content)
	ages=[2020-p['born']['year'] for p in players]
	return sum(ages)/len(ages)