import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="AI+数字化融合 | 极速出海", page_icon="🧠")
st.title("🧠 AI + 💪 数字化 = 完整方案")

st.markdown("""
<div style="text-align: center; font-size: 2rem; margin: 2rem 0;">
    🧠 <span style="color:#1e5f7a;">AI是大脑</span> 
    + 
    💪 <span style="color:#f3b33d;">数字化是手脚</span>
</div>
""", unsafe_allow_html=True)

# 对比表格
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

# 架构图
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
# --- 嵌入可查看的 Coze 工作流 ---
st.markdown("---")
st.subheader("⚙️ Coze 工作流实时演示")

# 您的 Coze 工作流链接
coze_url = "https://www.coze.cn/work_flow?space_id=7491136436608106536&workflow_id=7610438014247305225&force_stay=1"

# 创建选项卡，让用户选择查看方式
view_option = st.radio(
    "选择查看方式：",
    ["🔗 点击链接查看", "🖼️ 嵌入页面查看（需登录）"],
    horizontal=True
)

if view_option == "🔗 点击链接查看":
    st.markdown(f"""
    <div style="background-color: #f0f7fa; padding: 20px; border-radius: 10px; text-align: center;">
        <h4 style="color: #1e5f7a;">🤖 Coze 询盘分类工作流</h4>
        <p>点击下方按钮，在新标签页中打开工作流（可能需要登录 Coze 账号）。</p>
        <a href="{coze_url}" target="_blank">
            <button style="background-color: #1e5f7a; color: white; padding: 12px 30px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; font-weight: bold;">
                🔗 打开 Coze 工作流
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)
    
else:
    # 尝试用 iframe 嵌入
    st.markdown(f"""
    <div style="background-color: #f0f7fa; padding: 20px; border-radius: 10px;">
        <h4 style="color: #1e5f7a;">🤖 Coze 工作流嵌入视图</h4>
        <p style="color: #666; font-size: 0.9em;">ⓘ 如果页面显示需要登录，请先登录您的 Coze 账号。</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 嵌入 iframe（高度可调）
    st.markdown(f'<iframe src="{coze_url}" width="100%" height="600" style="border: 2px solid #1e5f7a; border-radius: 10px;"></iframe>', unsafe_allow_html=True)
    
    st.info("💡 提示：如果无法显示，请选择上方的“点击链接查看”方式。")
