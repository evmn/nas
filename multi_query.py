#!/usr/bin/python3
import csv
import tmdbsimple as tmdb

locale=['zh-CN', 'zh-TW', 'zh-HK','en', 'ja-JP', 'ko-KR']

def query(index, keyword, year=None):
	search = tmdb.Search()
	for Lang in locale:
		if year:
			response = search.multi(query=keyword, primary_release_year=year, language=Lang)
		else:
			response = search.multi(query=keyword, language=Lang)
		media_list = filter(search.results)
		record = len(media_list)
		if record >=1:
			break;
	if record < 1 :
		print('{:02d}.\t === {} 无tmdb记录 ==='.format(index, keyword))
	elif record == 1:
		metainfo = media_list[0]
		media_type = metainfo['media_type']
		info = read_info(metainfo, media_type)
		
		year = info['year']
		title = info['title']
		category = info['type']
		if year:
			print('{:02d}.{}\t{} ({})'.format(index, category, title, year))
		else:
			print('{:02d}.{}\t{}'.format(index, category, title))
	else:
		print('{:02d}.\t{} 在tmdb有{}条记录'.format(index, keyword, record))
		n = 1
		for metainfo in media_list:
			media_type = metainfo['media_type']
			info = read_info(metainfo, media_type)
			
			year = info['year']
			title = info['title']
			category = info['type']
			if year:
				print('\t\t{}.{}  {} ({})'.format(n, category, title, year))
			else:
				print('\t\t{}.{}  {}'.format(n, category, title ))
			n = n + 1
def filter(search_results):
	medias = []
	for metainfo in search_results:
		if metainfo['media_type'] in ['movie','tv']:
			medias.append(metainfo)
	return medias

def read_info(metainfo, media_type):
# media_type is in ['movie','tv']
	meta = dict()
	if media_type == 'movie':
		meta['type'] = '电影🎥'
		meta['title'] = metainfo['title']
		try:
			meta['year'] = metainfo['release_date'][0:4]
		except KeyError:
			meta['year'] = None
	elif media_type == 'tv':
		meta['type'] = '剧集  '
		meta['title'] = metainfo['name']
		try:
			meta['year'] = metainfo['first_air_date'][0:4]
		except KeyError:
			meta['year'] = None
	return meta


def main():
	# Use your own tmdb API_KEY, the following sample is invalid
	tmdb.API_KEY = '79e3306ff101fd99a612de079442bc44'
	with open('media.list','r') as csv_file:
		index = 0
		csv_reader = csv.reader(csv_file, delimiter='@')
		for row in csv_reader:
			keyword=row[0]
			year=row[1]
			index = index + 1
			query(index, keyword, year)

if __name__ == "__main__":
	main()
			
