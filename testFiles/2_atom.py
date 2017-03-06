import feedparser
d = feedparser.parse('xml/atom10.xml')
print(d.feed.title_detail)
u'First item title'
print(d.feed.link_detail)
u'http://example.org/item/1'
print(d.feed.subtitle_detail)
u'Watch out for <span>nasty tricks</span>'
print(d.feed.updated_detail)
u'Thu, 05 Sep 2002 00:00:01 GMT'
print(d.feed.id_detail)
