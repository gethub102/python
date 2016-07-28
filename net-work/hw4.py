import urllib
from BeautifulSoup import *

# url = raw_input('Enter - ')
url = 'http://python-data.dr-chuck.net/comments_289198.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
# for tag in tags:
#     # Look at the parts of a tag
#     print 'TAG:',tag
#     print 'URL:',tag.get('href', None)
#     print 'Contents:',tag.contents[0]
#     print 'Attrs:',tag.attrs

sum_number = 0.0
for tag in tags:
	sum_number += float(tag.contents[0])
print 'sum of number: ', sum_number
