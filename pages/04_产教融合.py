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
