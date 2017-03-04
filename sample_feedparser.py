import feedparser
import pprint

fo = open('xml10.py','w')

d = feedparser.parse("http://timesofindia.indiatimes.com/rssfeedstopstories.cms")

print(d['encoding'])
# pp=pprint.pformat(d,indent=4)
# qq=pprint.pformat(dict,indent=4)

# fo.write(pp)