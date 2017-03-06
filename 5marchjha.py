import feedparser
import pprint 
import json
fp=open("parsedfeed1.py","w")
d=feedparser.parse("http://timesofindia.indiatimes.com/rssfeedstopstories.cms")
print(json.loads(d))
# print(d)

