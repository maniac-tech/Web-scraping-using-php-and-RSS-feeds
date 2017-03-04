import feedparser
d = feedparser.parse('xml/rss2.0.xml')
print(d.entries[0].title)
u'First item title'
print(d.entries[0].link)
u'http://example.org/item/1'
print(d.entries[0].description)
u'Watch out for <span>nasty tricks</span>'
print(d.entries[0].published)
u'Thu, 05 Sep 2002 00:00:01 GMT'
print(d.entries[0].published_parsed)
(2002, 9, 5, 0, 0, 1, 3, 248, 0)
print(d.entries[0].id)