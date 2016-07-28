import re
words = open('sample-1.txt')
Sum = 0
Count = 0
for line in words:
	stuff = re.findall('[0-9]+[0-9.]*', line)
	for ele in stuff:
		Count += 1
		Sum += int(ele)
print 'Count', Count, 'Sum: ', Sum