import sys
import time

import requests as r
from operator import itemgetter


def api_testing():
	city = 'Izhevsk'
	limit = 5
	api_key = '11c0d3dc6093f7442898ee49d2430d20'
	url = f'http://api.openweathermap.org/geo/1.0/direct'
	params = {
		'q': city,
		'limit': limit,
		'appid': api_key
	}
	
	res = r.get(url,
				params=params)
	city_info = res.json()
	
	lat = city_info[0]['lat']
	lon = city_info[0]['lon']
	url = f'https://api.openweathermap.org/data/2.5/weather'
	params = {
		'lat': lat,
		'lon': lon,
		'units': 'metric',
		'appid': api_key
	}
	
	res = r.get(url,
				params=params)
	print(f'Температура в Ижевске (ну или чё ты там ввёл): {(res.json()["main"]["temp"])}')

# Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.
# Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
def interesting_number_check():
	for line in sys.stdin:
		line = line.strip()
		if line == 'break':
			break
		url = f'http://numbersapi.com/{line}/math?json=true'
		res = r.get(url)
		if (res.status_code == 200):
			print('Interesting' if res.json()['found'] else 'Boring')

# Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию о имени художника и годе рождения.
# Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке.
def get_artists():
	client_id = '4061eb6270cc833cb04d'
	client_secret = 'a63396aafc58cddcba8ae391919c0a59'
	token_request = r.post("https://api.artsy.net/api/tokens/xapp_token",
							data={
								"client_id": client_id,
								"client_secret": client_secret
							})
	token = token_request.json()['token']
	headers = {"X-Xapp-Token" : token}
	artists = list()
	with open(r"C:\Users\eyzmachine\Downloads\dataset_24476_4 (5).txt", 'r') as f:
		for line in f:
			time.sleep(1)
			line = line.strip()
			res = r.get(f"https://api.artsy.net/api/artists/{line}",
						 headers=headers)
			res.encoding = 'utf-8'
			if (res.status_code == 200):
				artist_json = res.json()
				artists.append({'name': artist_json['sortable_name'], 'year': artist_json['birthday']})
		artists = sorted(artists, key=itemgetter('year', 'name'))
	with open("answer.txt", "w", encoding='UTF-8') as f:
		for artist in artists:
			print(artist['name'], file=f)

get_artists()
