import requests

def get_news():
    # 这是一个专门为开发者提供的推特转发接口（示例，实际使用时可找稳定的 API）
    # 为了演示，我们使用一个稳定的第三方转换源
    url = "https://rsshub.app/twitter/user/prettybusy_KR?limit=5"
    
    try:
        # 伪装成浏览器去访问
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        
        # 这里我们利用一个黑科技：如果 RSSHub 挂了，我们尝试备用节点
        if response.status_code != 200:
            backup_url = "https://rss.dragonegg.moe/twitter/user/prettybusy_KR?limit=5"
            response = requests.get(backup_url, headers=headers, timeout=10)
        
        import feedparser
        data = feedparser.parse(response.text)
        return data.entries
    except:
        return []
