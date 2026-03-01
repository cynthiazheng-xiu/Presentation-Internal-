import streamlit as st
import plotly.graph_objects as go

# 页面配置
st.set_page_config(page_title="AI+数字化融合 | 极速出海", page_icon="🧠")

# 页面标题
st.title("🧠 AI + 💪 数字化 = 完整方案")

# 口号
st.markdown("""
<div style="text-align: center; font-size: 2rem; margin: 2rem 0;">
    🧠 <span style="color:#1e5f7a;">AI是大脑</span> 
    + 
    💪 <span style="color:#f3b33d;">数字化是手脚</span>
</div>
""", unsafe_allow_html=True)

# ===== 第一部分：AI vs 数字化对比表格 =====
st.subheader("📊 AI模块 vs 数字化模块")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🧠 AI模块")
    ai_data = {
        "模块": ["数字人直播", "Coze工作流"],
        "角色": ["思考、互动、获客", "判断、决策、回复"],
        "技术": ["AI数字人", "智能体+知识库"]
    }
    st.dataframe(ai_data, use_container_width=True, hide_index=True)

with col2:
    st.markdown("### 💪 数字化模块")
    digital_data = {
        "模块": ["报价系统", "PRA单证"],
        "角色": ["执行、计算、输出", "自动化、提效、落地"],
        "技术": ["Excel VBA / Python", "Power Automate"]
    }
    st.dataframe(digital_data, use_container_width=True, hide_index=True)

# ===== 第二部分：技术架构图 =====
st.markdown("---")
st.subheader("📐 技术架构图")

fig = go.Figure()

# 添加节点
fig.add_trace(go.Scatter(
    x=[0, 2, 4, 6, 8],
    y=[5, 5, 5, 5, 5],
    mode="markers+text",
    marker=dict(size=[40, 40, 40, 40, 40], color=["#f3b33d", "#1e5f7a", "#1e5f7a", "#f3b33d", "#f3b33d"]),
    text=["客户", "数字人(AI)", "Coze(AI)", "报价(数字化)", "PRA(数字化)"],
    textposition="bottom center",
    showlegend=False
))

# 添加连接线
for i in range(4):
    fig.add_shape(
        type="line",
        x0=i*2, y0=5,
        x1=(i+1)*2, y1=5,
        line=dict(color="#aaa", width=2, dash="dot")
    )

fig.update_layout(
    title="数据流向图",
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    height=300,
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

# ===== 第三部分：Coze工作流展示 =====
st.markdown("---")
st.subheader("⚙️ Coze 工作流演示")

# 简单的文字说明（确保这部分能显示）
st.markdown("""
<div style="background-color: #f0f7fa; padding: 20px; border-radius: 10px;">
    <h4 style="color: #1e5f7a;">🤖 Coze 询盘分类工作流</h4>
    <p><strong>功能</strong>：自动分类客户询盘，生成回复建议</p>
    <p><strong>效果</strong>：人工25分钟 → AI辅助2分钟</p>
    <p><strong>链接</strong>：<a href="https://www.coze.cn/work_flow?space_id=7491136436608106536&workflow_id=7610438014247305225&force_stay=1" target="_blank">点击查看工作流（需登录）</a></p>
</div>
""", unsafe_allow_html=True)

# ===== 第四部分：工作流价值总结 =====
st.markdown("---")
st.markdown("""
<div style="background-color: #e6f0f5; padding: 20px; border-radius: 10px;">
    <h4 style="color: #1e5f7a;">✨ Coze工作流价值</h4>
    <p>作为“AI大脑”的核心，Coze工作流实现：自动化询盘分类、智能回复生成、知识库积累、0成本部署。</p>
</div>
""", unsafe_allow_html=True)
