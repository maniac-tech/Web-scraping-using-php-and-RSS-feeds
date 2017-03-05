import feedparser
import pprint 

#creating a file for storage
fp=open("parsedfeed.py","w")
fe=open("formattedentries.py","w")
fl=open("formattedlist.py","w")


d=feedparser.parse("http://timesofindia.indiatimes.com/rssfeedstopstories.cms")

#prettu print
pp=pprint.pformat(d,indent=4)

#writing the feed to file 
fp.write(pp)

#formating entries section:
qq=pprint.pformat(d['entries'],indent=4)

#printing only the value of 'entries':
#print(d['entries'])

#storing the formatted entries into a file
fe.write(qq)

#storing the output of recovered value into a list:
list = d['entries']

#printing the list recovered from entries:
# print(list)

#formatting the list generated:
rr=pprint.pformat(list,indent=4)

#storing the formatted list into file:
fl.write(rr)

#printing the formated list
print(rr)
