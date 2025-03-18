import feedparser
d = feedparser.parse('https://feedparser.readthedocs.io/en/latest/examples/atom10.xml')
print(d['feed']['title'])
print(d.feed.title)
print(d.feed.link)
print(d.feed.description)
#print(d.feed.published)
#print(d.feed.published_parsed)
print(d.entries[0].published)
print(d.entries[0].published_parsed)
print(d.entries[0].id)

"""import feedparser

user_ownfeedlink = feedparser.parse('https://globalnation.inquirer.net/feed')
print(user_ownfeedlink.feed.title)
print(user_ownfeedlink.entries[0].description)
print(user_ownfeedlink.feed.link)"""

