import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_289195.xml'



url = serviceurl ;
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)


results = tree.findall('.//count')
num_sum = 0
for ret in results:
    try:
        print "Ret", ret.text
        num_sum += float(ret.text)
    except:
        pass
print 'Sum: ', num_sum
