import feedparser

def get_news():
    # 换成这个更官方、更稳的地址
    url = "https://rsshub.app/twitter/user/prettybusy/allow_emptycontent=1"
    
    # 加上一点“伪装”，让推特觉得我们是正常人在看
    data = feedparser.parse(url)
    
    if not data.entries:
        return []
    return data.entries[:5]
