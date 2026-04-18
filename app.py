import streamlit as st
from fetch_news import get_news

st.set_page_config(page_title="PrettyBusy 情报站", page_icon="🦋")

st.title("🦋 PrettyBusy 自动情报站")
st.write("不必翻墙，同步感受地狱的魅力！")

# 添加一个刷新按钮
if st.button('🚀 尝试同步最新海外情报'):
    with st.spinner('正在穿越时空搬运中...'):
        info = get_news()
        
        if not info:
            st.warning("⚠️ 哎呀，搬运梯子暂时断了（RSSHub 拥堵），请几分钟后再试，或者联系站长人工更新。")
        else:
            for post in info:
                st.markdown(f"### 📅 发布时间：{post.published}")
                
                # --- 核心黑科技：图片代理 ---
                # 这行代码会把推特图片链接换成国内能开的加速链接
                content = post.description.replace(
                    'https://pbs.twimg.com', 
                    'https://i.weserv.nl/?url=https://pbs.twimg.com'
                )
                
                # 显示抓取到的内容（文字+图片）
                st.markdown(content, unsafe_allow_html=True)
                st.write(f"[查看原文]({post.link})")
                st.divider()

st.info("💡 提示：如果自动更新失败，说明推特官方封锁较严，请稍后再试。")
