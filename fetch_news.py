import feedparser

def get_news():
    # 我们换一个更快的“搬运桥梁”地址
    url = "https://rss.dragonegg.moe/twitter/user/prettybusy"
    data = feedparser.parse(url)
    
    # 打印一下看看有没有拿到东西（这是给后台看的）
    if not data.entries:
        return []
    return data.entries[:5]
