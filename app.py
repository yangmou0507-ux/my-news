import streamlit as st

st.set_page_config(page_title="PrettyBusy 情报站", page_icon="🦋")

st.title("🦋 PrettyBusy 搬运站")
st.write("大家不用翻墙也能看消息啦！")

st.divider()

# --- 这里就是你发朋友圈的地方 ---
# 每一条情报你可以复制下面的格式

st.subheader("📅 最新情报：2024年4月18日")
st.image("这里贴图片的链接", caption="图片说明")
st.write("""
这里写你想对群友说的话，或者翻译好的推特内容。
比如：官方更新了新的角色立绘！大家快看！
""")

st.divider()

st.subheader("📅 往期回顾：2024年4月15日")
st.write("之前更新的消息内容...")
# ------------------------------

st.info("💡 站长提示：由于海外官网抓取不稳定，目前改为人工搬运，感谢大家支持！"
