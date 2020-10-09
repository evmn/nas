import csv
import tmdbsimple as tmdb
from datetime import datetime
tmdb.API_KEY = '79e3306ff10199a612de079442bc44'#自己到tmdb注册API_KEY
search = tmdb.Search()
with open('movie.csv','r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter='@')
	count = 0
	for row in csv_reader:
		keyword=row[0]
		year=row[1]
		count = count + 1
		if year:
			response = search.movie(query=keyword, primary_release_year=year, language='zh-CN')
		else:
			response = search.movie(query=keyword, language='zh-CN')

		record = len(search.results)
		if record < 1:
			print('{}.\t  === {} 无tmdb记录 ==='.format(count, keyword))
		elif record == 1:
			s = search.results[0]
			date = s['release_date']
			title = s['title']
			if date:
				dt = datetime.strptime(date, '%Y-%m-%d')
				print('{}.\t{} ({})'.format(count, title, dt.year))
			else:
				print('{}.\t{}'.format(count,title))
		else:
			print('{}.\t--- {} 在tmdb有{}条记录 ---'.format(count, keyword, record))
			n = 1
			for l in search.results:
				try:
					print('\t\t{}. {} ({})'.format(n, l['title'],l['release_date']))
				except KeyError:
					print('\t\t{}. {}'.format(n, l['title']))
				n = n + 1
			
