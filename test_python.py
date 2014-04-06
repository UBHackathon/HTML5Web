from datetime import datetime
import urllib
import urllib2
import json
from collections import namedtuple

response = urllib2.urlopen("http://hackerleague.org/api/v1/hackathons.json")

html_string =response.read()
utc_datetime = datetime.utcnow()
print utc_datetime

try:
	decoded = json.loads(html_string)

	result  =	filter(lambda x: x['location']['city'] =='Berlin', decoded)
	hack_time = filter(lambda x: datetime.strptime(x['start_time'], "%Y-%m-%dT%H:%M:%Sz") > utc_datetime, result)
	print hack_time

except (ValueError, KeyError, TypeError):
    print "JSON format error"
