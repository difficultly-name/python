import urllib.request
from bs4 import BeautifulSoup
import pymysql

namelist = []
def get_html(url):
	"""获取HTML代码"""
	res = urllib.request.urlopen(url)
	html = res.read().decode()

	return html
def parse_html(htmllife):
	"""解析HTML，获取名字列表"""
	mysoup = BeautifulSoup(htmllife,'html.parser')
	class_zone = mysoup.find('div', attrs={'class':'CourseList_courseList'})
	class_list = class_zone.find_all('div', attrs={'class':'CourseListItem_info'})
	for i in class_list:
		name = i.find('div', attrs={'class':'text-ellipsis-line-2 CourseListItem_title'}).getText()
		namelist.append(name)
for n in range(1,11):
	htmllife = get_html(url = 'https://vip.open.163.com/courses/?firstId=-1&source=pcphp_subView_more&page='+str(n))
	parse_html(htmllife)
print(namelist)