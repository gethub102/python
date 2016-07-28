import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.py4inf.com', 80))

mysocket.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
	data = mysocket.recv(512)
	if (len(data) < 1) :
		break
	print data
mysocket.close()

print "------urllib-----"

import urllib
splitfile = fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
	print line.strip()

splitfile = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
counts = dict()
for lines in splitfile:
	words = lines.split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1
print counts