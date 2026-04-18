import streamlit as st
from fetch_news import get_news

st.title("🦋 PrettyBusy 搬运站")
st.write("大家不用翻墙也能看消息啦！")

if st.button('点我刷新情报'):
    with st.spinner('正在同步海外情报...'):
        info = get_news()
        if not info:
            st.warning("⚠️ 搬运梯子暂时断了，请过几分钟再点一次。")
        else:
            for post in info:
                st.markdown(f"### 📅 时间：{post.published}")
                # 魔法代理：让图片在国内正常显示
                content = post.description.replace('https://pbs.twimg.com', 'https://i.weserv.nl/?url=https://pbs.twimg.com')
                st.markdown(content, unsafe_allow_html=True)
                st.divider()
