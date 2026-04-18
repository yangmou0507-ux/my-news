import feedparser

def get_news():
    # 这个链接就是把推特变成网页能读的格式
    url = "https://rsshub.app/twitter/user/prettybusy"
    data = feedparser.parse(url)
    return data.entries[:5] # 只拿最近5条
