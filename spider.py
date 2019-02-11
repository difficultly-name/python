import urllib.request
from bs4 import BeautifulSoup

movielist = []
url = "https://movie.douban.com/top250"


def get_html(url):
	res = urllib.request.urlopen(url)
	html = res.read().decode()

	return html


def parse_html(htmlfile):
	mysoup = BeautifulSoup(htmlfile,'html.parser')
	movie_zone = mysoup.find('ol')
	movie_list = movie_zone.find_all('li')
	for movie in movie_list:
		movie_name = movie.find('span', attrs = {'class':'title'} ).getText()
		movielist.append(movie_name)
	nextpage = mysoup.find('span',attrs = {'class':'next'}).find('a')
	if nextpage != None:
		new_url = url + nextpage['href']
		parse_html(get_html(new_url))


parse_html(get_html(url))
print(movielist)


