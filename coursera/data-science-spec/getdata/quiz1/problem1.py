import pandas
import urllib2

def send_request(url):
	request = urllib2.Request(url)
	return urllib2.urlopen(request).read()

table = send_request('https://d396qusza40orc.cloudfront.net/getdata%2Fwksst8110.for')

lines = table.split('\n')
lines = lines[4:]

total = 0

for line in lines:
	break
	print line
	pieces = line.split('     ')
	if len(pieces) != 5:
		break
	piece = pieces[2]
	print piece
	if '-' in piece:
		value = piece.split('-')[0]
	else:
		value = piece.split(' ')[0]
	total = total + float(value)

print total

table = pandas.read_table('https://d396qusza40orc.cloudfront.net/getdata%2Fwksst8110.for ',
	skiprows=4)

print table