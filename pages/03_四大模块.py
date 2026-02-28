import streamlit as st

st.set_page_config(page_title="四大模块 | 极速出海", page_icon="🛠️")
st.title("🛠️ 四大核心技术模块")

tabs = st.tabs(["🤖 数字人直播", "🧠 Coze工作流", "💰 报价系统", "📄 PRA单证"])

with tabs[0]:
    st.header("数字人直播——24小时智能获客")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **功能**：
        - 24小时不间断直播
        - 多语言自动切换
        - 智能问答互动
        - 留资引导
        
        **成本**：200元/月
        """)
    with col2:
        st.markdown("""
        **对比**：
        - 人工直播：8小时/天，1万/月
        - 数字人直播：24小时/天，200元/月
        - 转化率提升：2.5% → 10%
        """)
    st.image("https://via.placeholder.com/600x300/1e5f7a/ffffff?text=AI+数字人演示画面", use_container_width=True)

with tabs[1]:
    st.header("Coze工作流——智能询盘分类")
    st.markdown("""
    **工作流程**：
    1. 接收客户邮件/询盘
    2. 关键词识别与意图判断
    3. 匹配知识库规则
    4. 生成分类标签+建议话术+回复草稿
    
    **效果**：
    - 人工25分钟 → AI辅助2分钟
    - 错误率26% → 2%
    - 成本0元（Coze免费版）
    """)

with tabs[2]:
    st.header("报价系统——双方案并行")
    option = st.radio("选择版本查看", ["Excel+VBA版", "Python+Streamlit版"])
    
    if option == "Excel+VBA版":
        st.markdown("""
        **特点**：不改习惯，只改工具
        - 产品下拉菜单
        - 汇率自动抓取
        - 一键生成PDF
        - 成本0元（Excel已有）
        """)
    else:
        st.markdown("""
        **特点**：AI辅助开发，更智能
        ```python
        # 大模型帮我写的代码
        import streamlit as st
        st.title("AI价到报价系统")
        procurement = st.number_input("采购成本")
        freight = st.number_input("运输成本")
        total = procurement + freight
        st.metric("总报价", f"$ {total:,.2f}")
