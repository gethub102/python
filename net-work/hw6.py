import urllib
import json
from BeautifulSoup import *

url = raw_input('Enter - ')
#url = 'http://python-data.dr-chuck.net/comments_42.json'
input = urllib.urlopen(url).read(); #this is a string obj
info = json.loads(input)
ret_sum = 0;
print 'Count: ', len(info["comments"])
for item in info["comments"]:
	ret_sum += item['count']

print 'Sum: ', ret_sum



