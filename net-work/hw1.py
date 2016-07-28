import re


print("Hello World")

# ^X.*: -- X-Siver:
# ^X-\S+: -- X-Siver:

hand = open("mbox-short.txt")
for line in hand:
	line = line.rstrip()
	if line.find("From:") >= 0:
		print(line)

hand = open("mbox-short.txt")
for line in hand:
	line = line.rstrip()
	if re.search('From:', line):
		print line


x = 'My 2 favorite numbers are 19 and 15'
y = re.findall('[0-9]+', x)
print(y)

y = re.findall('[AEIOU]+', x)
print(y)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
y = re.findall('^F.+?:', x)
print(y)

x = 'From lwb@mail.nankai.edu.cn Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)
y = re.findall('^From \S+@\S+', x)
print(y)

data = 'From stephen.marquard@uct.ac.za Sat Jan'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print sppos

host = data[atpos+1 : sppos]
print host

words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

import re
line =  'From stephen.marquard@uct.ac.za Sat Jan'
y = re.findall('^From .*@([^ ]*)', line)
print(y)

import re 
hand = open("smaple-1.txt")
numlist = list()
for line in hand:
	line = line.rstrip()
	stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
	if len(stuff) != 1 : continue
	num = float(stuff[0])
	numlist.append(num)
print 'Maxinum: ', max(numlist)