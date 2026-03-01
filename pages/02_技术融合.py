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

# ===== 第三部分：Coze工作流展示（新添加的部分）=====
st.markdown("---")
st.subheader("⚙️ Coze 工作流演示")

# 您的 Coze 工作流链接
coze_url = "https://www.coze.cn/work_flow?space_id=7491136436608106536&workflow_id=7610438014247305225&force_stay=1"

# 创建三选项卡
tab1, tab2, tab3 = st.tabs(["📸 工作流截图", "🎥 功能说明", "🔗 在线链接"])

with tab1:
    st.markdown("### 工作流结构设计")
    st.markdown("""
    **Coze 智能体工作流包含以下节点：**
    
    1. **输入节点**：接收客户邮件/询盘
    2. **意图识别节点**：关键词匹配（FOB/CIF/DDP/认证等）
    3. **知识库查询节点**：匹配产品目录、报价规则
    4. **话术生成节点**：根据客户类型生成回复草稿
    5. **输出节点**：结构化输出（分类+建议+草稿）
    """)
    
    # 这里放一个占位图，你可以替换成真实截图
    st.image("https://via.placeholder.com/800x300/1e5f7a/ffffff?text=Coze+工作流结构图+（请替换为真实截图）", use_container_width=True)
    st.caption("图：Coze 询盘分类工作流节点设计")

with tab2:
    st.markdown("### 工作流运行效果")
    
    st.markdown("""
    **测试输入**：
    > "Hi, I'm interested in your baijiu. Please quote CIF Los Angeles price for 200 cases."
    
    **AI 处理结果**：
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**分类标签**：CIF报价询盘")
        st.info("**客户意图**：询CIF洛杉矶价，200箱")
    with col2:
        st.success("**建议话术**：建议报含运费保险的价格，可附产品规格书")
        st.success("**回复草稿**：自动生成英文回复")
    
    st.markdown("""
    **效率对比**：
    - 人工处理：25分钟
    - AI辅助：**2分钟**
    - 错误率：26% → **2%**
    """)

with tab3:
    st.markdown("### 在线查看完整工作流")
    st.markdown(f"""
    <div style="background-color: #f0f7fa; padding: 30px; border-radius: 10px; text-align: center;">
        <p style="font-size: 1.1rem;">点击下方按钮，在 Coze 平台查看完整工作流：</p>
        <p style="color: #666; font-size: 0.9rem;">ⓘ 需要登录您的 Coze 账号才能查看</p>
        <a href="{coze_url}" target="_blank">
            <button style="background-color: #1e5f7a; color: white; padding: 15px 40px; border: none; border-radius: 5px; cursor: pointer; font-size: 18px; font-weight: bold;">
                🔗 打开 Coze 工作流
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

# ===== 第四部分：工作流价值总结 =====
st.markdown("---")
st.markdown("""
<div style="background-color: #e6f0f5; padding: 20px; border-radius: 10px; border-left: 5px solid #f3b33d;">
    <h4 style="color: #1e5f7a; margin-top: 0;">✨ Coze工作流在项目中的价值</h4>
    <p>作为 <strong>“AI大脑”</strong> 的核心组成部分，Coze工作流实现了：</p>
    <ul>
        <li><strong>自动化询盘分类</strong>：秒级识别客户意图</li>
        <li><strong>智能回复生成</strong>：减少人工重复劳动</li>
        <li><strong>知识库积累</strong>：每次询盘都在优化模型</li>
        <li><strong>0成本部署</strong>：Coze免费版完全够用</li>
    </ul>
</div>
""", unsafe_allow_html=True)
