import streamlit as st
from PIL import Image
import pandas as pd

# 页面配置
st.set_page_config(
    page_title="极速出海 | AI赋能的报价履约协同助手-郑秀英| 郑秀英",
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
        - **获客难**：70%企业缺运营人才 → 24小时数字人直播
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
# ===== 指导教师风采：郑秀英 =====
st.markdown("---")
st.subheader("👩‍🏫 指导教师：郑秀英")

# 创建一个左右布局
col1, col2 = st.columns([1, 3])

with col1:
    # 用背景色块代替照片
    st.markdown("""
    <div style="background-color: #1e5f7a; width: 120px; height: 120px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto;">
        <span style="color: white; font-size: 48px; font-weight: bold;">郑</span>
    </div>
    """, unsafe_allow_html=True)
    st.caption("郑秀英 老师")

with col2:
    st.markdown("""
    **郑秀英** 讲师 | 贵州航天职业技术学院基础科学系  
    **专业背景**：四川大学国际贸易专业经济学学士  
    **行业经验**：10+年知名企业实战经验（深圳鸿富锦、上海惠普、安永全球商务服务等），曾任采购主管、项目主管

    **🏆 核心荣誉（省教育厅及以上奖项）**：
    """)
    # 指导教师成绩总结（注意：这里是正确的三个引号！）
st.info("""
🏆 **指导教师战绩**：近三年累计获得**贵州省教育厅颁发的省级技能大赛奖项6项**，其中**一等奖2项，二等奖4项**。
多次荣获学院“优秀教师”称号（2021、2022、2024），累计指导学生获省级以上奖项20余项。
""")
    
    # 荣誉列表
    honors = [
        "**2021** 贵州省职业院校技能大赛高职组‘英语口语’赛项 **一等奖**（指导老师）",
        "**2023** 贵州省职业院校技能大赛高职组‘跨境电子商务’赛项 **一等奖**（指导老师）",
        "**2024** 贵州省职业院校技能大赛‘互联网+国际经济与贸易’赛项 **二等奖**（指导老师）",
        "**2023** 贵州省职业院校技能大赛‘互联网+国际贸易综合技能’赛项 **二等奖**（指导老师）",
        "**2025** 贵州省职业院校技能大赛‘互联网+国际经济与贸易’赛项 **二等奖**（指导老师）",
        "**2025** 中国国际大学生创新大赛贵州省省赛 **银奖**（指导老师）"
    ]
    for honor in honors:
        st.markdown(f"- {honor}")  # 加了个小圆点，更好看
