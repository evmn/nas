#!/usr/bin/python3
import csv
import tmdbsimple as tmdb
from datetime import datetime
tmdb.API_KEY = '79e3306ff10199a612de079442bc44'#自己到tmdb注册API_KEY
search = tmdb.Search()
with open('tv.csv','r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter='@')
	count = 0
	for row in csv_reader:
		keyword=row[0]
		year=row[1]
		count = count + 1
		if year:
			response = search.tv(query=keyword, first_air_date_year=year, language='zh-CN')
		else:
			response = search.tv(query=keyword, language='zh-CN')

		record = len(search.results)
		if record < 1:
			print('{}.\t=== {} 无tmdb记录 ==='.format(count, keyword))
		elif record == 1:
			s = search.results[0]
			title = s['name']
			try:
				year = s['first_air_date'][0:4]
				print('{}.\t{} ({})'.format(count, title, year))
			except KeyError:
				print('{}.\t{}'.format(count,title))
		else:
			print('{}.\t--- {} 在tmdb有{}条记录 ---'.format(count, keyword, record))
			n = 1
			for l in search.results:
				try:
					print('\t\t{}. {} ({})'.format(n, l['name'],l['first_air_date']))
				except KeyError:
					print('\t\t{}. {}'.format(n, l['name']))
				n = n + 1
			
