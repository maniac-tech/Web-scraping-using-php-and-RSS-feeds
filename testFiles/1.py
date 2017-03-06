import feedparser
rawdata = """<rss version="2.0"
	<channel>
	<title>Sample feed</title>
	</channel>
	</rss>
"""
d=feedparser.parse(rawdata)
print (d['feed']['title'])