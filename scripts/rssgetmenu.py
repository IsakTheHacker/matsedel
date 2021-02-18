import feedparser

def getmenu():
    NewsFeed = feedparser.parse("https://skolmaten.se/nya-elementar/rss/days/")
    return NewsFeed.entries[0].summary.split("<br />")