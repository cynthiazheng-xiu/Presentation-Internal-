import streamlit as st

st.set_page_config(page_title="四大模块 | 极速出海", page_icon="🛠️")
st.title("🛠️ 四大核心技术模块")

tabs = st.tabs(["🤖 数字人直播", "🧠 Coze工作流", "💰 报价系统", "📄 PRA单证"])

with tabs[0]:
    st.header("数字人直播——24小时智能获客")
    st.markdown("""
    **功能**：
    - 24小时不间断直播
    - 多语言自动切换
    - 智能问答互动
    """)

with tabs[1]:
    st.header("Coze工作流——智能询盘分类")
    st.markdown("""
    **工作流程**：
    1. 接收客户邮件/询盘
    2. 关键词识别与意图判断
    3. 生成分类标签+建议话术+回复草稿
    **效果**：人工25分钟 → AI辅助2分钟
    """)

with tabs[2]:
    st.header("报价系统——双方案并行")
    st.markdown("""
    **Excel+VBA版**：不改习惯，2分钟报价
    **Python版**：AI辅助开发，更智能
    """)

with tabs[3]:
    st.header("PRA单证——3秒自动填单")
    st.markdown("""
    **Power Automate Desktop流程**：
    - 录制复制粘贴动作
    - 优化选择器+等待
    - 一键运行，3秒填完20个字段
    **效果**：人工15分钟 → 3秒，错误率26% → 2%
    """)
