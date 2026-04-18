import streamlit as st
from fetch_news import get_news

st.title("🦋 PrettyBusy 搬运站")
st.write("大家不用翻墙也能看消息啦！")

if st.button('点我刷新情报'):
    info = get_news()
    for post in info:
        st.markdown(f"### 📅 时间：{post.published}")
        # 下面这一行会把文字和图片都显示出来
        st.markdown(post.description, unsafe_allow_html=True)
        st.divider()
