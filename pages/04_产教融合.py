import streamlit as st

st.set_page_config(page_title="产教融合 | 极速出海", page_icon="🤝")
st.title("🤝 产教融合·真实落地")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### ✅ 学生已掌握技能")
    st.markdown("""
    - 🎤 数字人运营
    - 🧠 AI工作流配置
    - 📊 Excel自动化
    - 🤖 PRA流程优化
    """)
    
    st.markdown("### 🏆 团队分工")
    team_data = {
        "角色": ["队长", "营销专员", "运营专员", "技术专员"],
        "主攻模块": ["整体把控", "数字人直播", "Coze工作流", "报价系统+PRA"]
    }
    st.dataframe(team_data, use_container_width=True, hide_index=True)

with col2:
    st.markdown("### 🤝 企业合作")
    
    st.markdown("""
    **贵州遵礼外贸有限公司**
    - 4名学生正在实习
    - 深入了解行业痛点
    
    **贵州一码进出口有限责任公司**
    - 已见面3次
    - 正在洽谈合作开发报价模板
    
    **产业价值**
    - 63.64%企业想要的本地产业带实战案例
    - 我们做出来了！
    """)

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: #f0f7fa; border-radius: 20px;">
    <h3 style="color: #1e5f7a;">指导老师承诺</h3>
    <p style="font-size: 1.2rem;">全程跟训 · 资源协调 · 心理疏导</p>
    <p style="font-style: italic; margin-top: 1rem;">“项目用60分钟证明：AI+数字化，真的能让小微外贸‘极速出海’。”</p>
    <p>—— 郑秀英</p>
</div>
""", unsafe_allow_html=True)
# ===== 指导教师风采 =====
st.markdown("---")
st.subheader("👩‍🏫 指导教师：郑秀英")

# 创建两列布局
col1, col2 = st.columns([1, 2])

with col1:
    # 这里可以放老师照片，如果没有就用占位图
    st.image("https://via.placeholder.com/150/1e5f7a/ffffff?text=郑秀英", width=150)
    st.caption("郑秀英 老师")

with col2:
    st.markdown("""
    **简介**：
    讲师，贵州航天职业技术学院基础科学系教师。四川大学国际贸易专业经济学学士，拥有10+年知名企业实战经验（深圳鸿富锦、上海惠普、安永全球商务服务等），曾任采购主管、项目主管。
    
    **核心荣誉（省教育厅获奖）**：
    """)
    
    # 用表格展示省教育厅获奖
    honor_data = {
        "年份": ["2023", "2021", "2025", "2024", "2025"],
        "获奖项目": [
            "贵州省职业院校技能大赛高职组'跨境电子商务'赛项一等奖",
            "贵州省职业院校技能大赛高职组'英语口语'赛项一等奖",
            "中国国际大学生创新大赛贵州省省赛银奖",
            "贵州省职业院校技能大赛高职组'互联网+国际经济与贸易'赛项二等奖",
            "贵州省职业院校技能大赛高职组'互联网+国际经济与贸易'赛项二等奖"
        ],
        "级别": ["省教育厅", "省教育厅", "省教育厅", "省教育厅", "省教育厅"]
    }
    st.dataframe(honor_data, use_container_width=True, hide_index=True)

# 其他竞赛成果
st.markdown("""
**更多指导成果**：
- 多次指导学生在"OCALE全国跨境电商创新创业能力大赛"获二等奖
- 多次指导学生在"Shopee杯"跨境电商大赛获区域赛二等奖、全国总决赛优秀奖
- 多次荣获学院"优秀教师"称号（2021、2022、2024）
""")
