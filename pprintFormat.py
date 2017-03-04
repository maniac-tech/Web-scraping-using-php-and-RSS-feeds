import pprint
import feedparser

d = feedparser.parse("http://timesofindia.indiatimes.com/rssfeedstopstories.cms")
dictionary={
	'Yolo':'Yolo'
}
pp=pprint.pformat(d)
pprint.pprint(d)
