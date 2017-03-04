import feedparser
d = feedparser.parse("https://pythonhosted.org/feedparser/")

print(d.feed)