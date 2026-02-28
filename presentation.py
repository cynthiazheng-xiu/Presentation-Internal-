import streamlit as st
from PIL import Image
import pandas as pd

# 页面配置
st.set_page_config(
    page_title="极速出海 | AI赋能的报价履约协同助手",
    page_icon="🚢",
    layout="wide"
)

# 自定义CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #1e5f7a;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #f3b33d;
        text-align: center;
        margin-bottom: 2rem;
    }
    .slogan {
        font-size: 1.8rem;
        font-weight: 600;
        text-align: center;
        color: #0a3142;
        background: linear-gradient(90deg, #e6f0f5, #ffffff);
        padding: 1rem;
        border-radius: 50px;
        margin: 2rem 0;
    }
    .stat-card {
        background-color: #f8fbfd;
        border-left: 5px solid #1e5f7a;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# 头部
st.markdown('<div class="main-header">🚢 极速出海</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">AI赋能的报价履约协同助手</div>', unsafe_allow_html=True)

# 口号
st.markdown('<div class="slogan">快速 · 精准 · 协同</div>', unsafe_allow_html=True)

# 项目简介
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 🌟 项目简介")
        st.markdown("""
        **极速出海** 是一个专为小微外贸企业设计的**AI+数字化报价履约协同助手**，针对三大核心痛点：
        
        - **报价慢**：40%企业报价半天以上 → 2分钟报价
        - **单证错**：26%单证错误率 → 3秒填单，错误率2%
        - **获客难**：70%企业缺运营人才 → 24小时数字人直播，成本200元/月
        """)
        
        st.markdown("### 🛠️ 核心技术模块")
        tech_data = pd.DataFrame({
            "模块": ["数字人直播", "Coze工作流", "报价系统", "PRA单证"],
            "技术属性": ["🧠 AI", "🧠 AI", "💪 数字化", "💪 数字化"],
            "核心功能": ["24小时智能获客", "询盘自动分类回复", "2分钟极速报价", "3秒自动填单"]
        })
        st.dataframe(tech_data, use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown("### 📊 核心数据")
        st.markdown("""
        <div class="stat-card">
            <h1 style="color: #1e5f7a; font-size: 2.5rem;">40%</h1>
            <p>企业报价半天以上 → <span style="color:#f3b33d; font-weight:bold;">2分钟</span></p>
        </div>
        <div class="stat-card">
            <h1 style="color: #1e5f7a; font-size: 2.5rem;">26%</h1>
            <p>单证错误率 → <span style="color:#f3b33d; font-weight:bold;">2%</span></p>
        </div>
        <div class="stat-card">
            <h1 style="color: #1e5f7a; font-size: 2.5rem;">70%</h1>
            <p>企业缺人 → <span style="color:#f3b33d; font-weight:bold;">24h直播</span></p>
        </div>
        """, unsafe_allow_html=True)

# 导航提示
st.markdown("---")
st.markdown("### 👈 请从左侧边栏选择页面查看详情")
st.markdown("""
- **📊 三组数字**：调研数据深度解读
- **🧠 AI+数字化融合**：技术架构详解
- **🛠️ 四大模块**：各模块功能演示
- **🤝 产教融合**：团队与企业合作
""")
