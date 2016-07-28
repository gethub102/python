import urllib
from BeautifulSoup import *
url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

tags = soup('a')
count = 0
for tag in tags:
	count += 1
	if count > 3:
		break;
	if count == 3:
		count = 0
		html1 = urllib.urlopen(tag.get('href', None)).read()
		soup1 = BeautifulSoup(html1)
		tags1 = soup1('a')
		for tag1 in tags1:
			count += 1
			if count > 3:
				break;
			if count == 3:
				count = 0
				html2 = urllib.urlopen(tag1.get('href', None)).read()
				soup2 = BeautifulSoup(html2)
				tags2 = soup2('a')
				for tag2 in tags2:
					count += 1
					if count > 3:
						break;
					if count == 3:
						count = 0
						html3 = urllib.urlopen(tag2.get('href', None)).read()
						soup3 = BeautifulSoup(html3)
						tags3 = soup3('a')
						for tag3 in tags3:
							count += 1
							if count > 3:
								break;
							if count == 3:
								print tag3.get('href', None)

# def function(list_url):
# 	list_html = urllib.urlopen(list_url).read()
# 	list_soup = BeautifulSoup(list_html)
# 	tags = soup('a')
# 	return tags[4].get('href', None)
		