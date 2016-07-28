import urllib
from BeautifulSoup import *

url = raw_input ('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

print soup.prettify() # format print the source file
soup.find_all('a') # this result is a list

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes

tags = soup('a')

for tag in tags:
	print tag.get('href', None) # default value is none: if href = #, I think it will return none
	print tag.tex
	if "http" in tag.get('href'):
		print "<a href='%s'>%s</a>" %(tag.get('href'), tag.text)

a_data = soup.find_all("div", {"class", "info"})
for item in g_data:
	print item.text
	print item.content[0].text
	print item.content[1].text
	print item.content[0].text.find_all('a', {'class': "business-name"})[0].text
	print item.content[1].text.find_all('p', {'class': 'adr'})[0].text
	try:
		print item.content[0].text.find_all('span', {'itemprop': "adressLocality"})[0].text.replace(',', '')
	except:
		pass
	try:
		print item.content[1].text.find_all('li', {'class': 'primary'})[0].text
	except:
		pass