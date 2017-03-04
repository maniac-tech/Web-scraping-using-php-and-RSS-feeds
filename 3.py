import feedparser
d = feedparser.parse('xml/rss2.0.xml')
print(d.entries[0].title)

print(d.entries[0].link)

print(d.entries[0].description)

print(d.entries[0].published)

print(d.entries[0].published_parsed)

print(d.entries[0].id)