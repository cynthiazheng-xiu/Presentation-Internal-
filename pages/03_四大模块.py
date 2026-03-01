import streamlit as st

st.set_page_config(page_title="四大模块 | 极速出海", page_icon="🛠️")
st.title("🛠️ 四大核心技术模块")

tabs = st.tabs(["🤖 数字人直播", "🧠 Coze工作流", "💰 报价系统", "📄 PRA单证"])

# ===== 选项卡1：数字人直播 =====
with tabs[0]:
    st.header("数字人直播——24小时智能获客")
    st.markdown("""
    **功能**：
    - 24小时不间断直播
    - 多语言自动切换
    - 智能问答互动
    """)

# ===== 选项卡2：Coze工作流 =====
with tabs[1]:
    st.header("Coze工作流——智能询盘分类")
    
    # 工作流链接
    coze_url = "https://www.coze.cn/work_flow?space_id=7491136436608106536&workflow_id=7610438014247305225&force_stay=1"
    
    st.markdown(f"""
    **工作流程**：
    1. 接收客户邮件/询盘
    2. 关键词识别与意图判断
    3. 生成分类标签+建议话术+回复草稿
    
    **效果**：人工25分钟 → AI辅助2分钟
    """)
    
    # Coze工作流展示区域
    st.markdown("---")
    st.subheader("⚙️ Coze 工作流演示")
    
    st.markdown(f"""
    <div style="background-color: #f0f7fa; padding: 20px; border-radius: 10px;">
        <h4 style="color: #1e5f7a;">🤖 Coze 询盘分类工作流</h4>
        <p><strong>功能</strong>：自动分类客户询盘，生成回复建议</p>
        <p><strong>效果</strong>：人工25分钟 → AI辅助2分钟</p>
        <p><strong>链接</strong>：<a href="{coze_url}" target="_blank">点击查看工作流（需登录）</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    # 工作流价值总结
    st.markdown("---")
    st.markdown("""
    <div style="background-color: #e6f0f5; padding: 20px; border-radius: 10px;">
        <h4 style="color: #1e5f7a;">✨ Coze工作流价值</h4>
        <p>作为“AI大脑”的核心，Coze工作流实现：自动化询盘分类、智能回复生成、知识库积累、0成本部署。</p>
    </div>
    """, unsafe_allow_html=True)

# ===== 选项卡3：报价系统 =====
with tabs[2]:
    st.header("报价系统——双方案并行")
    st.markdown("""
    **Excel+VBA版**：不改习惯，2分钟报价
    **Python版**：AI辅助开发，更智能
    """)

# ===== 选项卡4：PRA单证 =====
with tabs[3]:
    st.header("PRA单证——3秒自动填单")
    st.markdown("""
    **Power Automate Desktop流程**：
    - 录制复制粘贴动作
    - 优化选择器+等待
    - 一键运行，3秒填完20个字段
    
    **效果**：人工15分钟 → 3秒，错误率26% → 2%
    """)
