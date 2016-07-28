import urllib
from BeautifulSoup import *
# url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
url = 'http://python-data.dr-chuck.net/known_by_Aayan.html'


def get_link(list_url, _pos):
	list_html = urllib.urlopen(list_url).read()
	list_soup = BeautifulSoup(list_html)
	tags = list_soup('a')
	pos = _pos - 1
	url = tags[pos].get('href', None)
	return url



def get_loop_link(pos, count_, url):
	count = 0
	while count < count_:
		count += 1
		url = get_link(url, pos)
		print url


print url 
# get_loop_link(3, 4, url)
get_loop_link(18, 7, url)