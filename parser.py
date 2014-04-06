
import json
import urllib
import urllib2

response = urllib2.urlopen("http://hackerleague.org/api/v1/hackathons.json")


html_string =response.read()
try:
	decoded = json.loads(html_string)
	print decoded[0]['location']['city']
except (ValueError, KeyError, TypeError):
    print "JSON format error"
#print html_string