import feedparser

user_ownLink = input("Enter your feed link here: ")
#Example link: https://globalnation.inquirer.net/feed

d = feedparser.parse(user_ownLink)
print(d.feed.title)
print(f"Today, {d.entries[0].published}. News Title: {d.entries[1].title}")
print(d.entries[0].description)
print(d.feed.link)

