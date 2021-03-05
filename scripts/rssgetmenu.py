import feedparser
import sys

def getmenu():
	NewsFeed = feedparser.parse("https://skolmaten.se/nya-elementar/rss/days/")
	try:
		return NewsFeed.entries[0].summary.split("<br />")
	except IndexError:
		print("Matsedeln kunde inte hittas!")
		sys.exit(1)