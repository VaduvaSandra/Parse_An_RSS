from bs4 import BeautifulSoup
import requests

url = requests.get('https://rss.nytimes.com/services/xml/rss/nyt/World.xml')

soup = BeautifulSoup(url.content, 'xml')
items = soup.find_all('item')

for item in items:
    title = item.title.text
    creator = item.creator.text
    pubDate = item.pubDate.text
    description = item.description.text

    print(f"Title: {title}\n\nCreator: {creator}\n\nPubDate: {pubDate}\n\nDescription: {description}\n\n---------------------\n\n")

x, y, z = input("Input: ").split('.')

print("Major = ", x)
print("Minor = ", y)
print("BugFix = ", z)
