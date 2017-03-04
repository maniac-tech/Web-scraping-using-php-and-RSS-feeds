import feedparser
d = feedparser.parse ("xml/rss2.0.xml")
print (d.feed.title)
print (d.feed.link)
print (d.feed.description)