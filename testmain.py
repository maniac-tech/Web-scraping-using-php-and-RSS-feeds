import feedparser
import pprint 
import json
fp=open("parsedfeed1.py","w")
d=feedparser.parse("http://timesofindia.indiatimes.com/rssfeedstopstories.cms")
#trying to deserialize hte json data
print(json.loads(d))
# print(d)

