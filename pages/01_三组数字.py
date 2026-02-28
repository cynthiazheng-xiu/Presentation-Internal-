import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="三组数字 | 极速出海", page_icon="📊")
st.title("📊 三组数字·项目灵魂")
st.caption("数据来源：遵义11家小微外贸企业真实问卷")

# 数据可视化
col1, col2, col3 = st.columns(3)

with col1:
    fig1 = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = 40,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "报价半天以上 (%)"},
        delta = {'reference': 100, 'valueformat': ".0f"},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "#1e5f7a"},
            'steps': [
                {'range': [0, 40], 'color': "#e6f0f5"},
                {'range': [40, 100], 'color': "#f8d7da"}],
            'threshold': {
                'line': {'color': "#f3b33d", 'width': 4},
                'thickness': 0.75,
                'value': 40}}))
    fig1.update_layout(height=250)
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown("**我们解决：2分钟报价**")

with col2:
    fig2 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 26,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "单证错误率 (%)"},
        gauge = {
            'axis': {'range': [None, 30]},
            'bar': {'color': "#dc3545"},
            'steps': [
                {'range': [0, 2], 'color': "#d4edda"},
                {'range': [2, 26], 'color': "#fff3cd"}],
            'threshold': {
                'line': {'color': "#f3b33d", 'width': 4},
                'thickness': 0.75,
                'value': 2}}))
    fig2.update_layout(height=250)
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("**我们解决：3秒填单，2%错误率**")

with col3:
    fig3 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 70,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "缺运营人才 (%)"},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "#1e5f7a"},
            'steps': [
                {'range': [0, 70], 'color': "#e6f0f5"},
                {'range': [70, 100], 'color': "#f8d7da"}]}))
    fig3.update_layout(height=250)
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown("**我们解决：24小时数字人直播，成本200元/月**")

# 详细数据表格
st.markdown("---")
st.subheader("📋 调研数据详情")

data = pd.DataFrame({
    "指标": ["报价时间>半天", "专业软件使用率", "单证错误率", "无IT人员", "缺运营人才", "预算1000-3000元"],
    "比例": ["40%", "0%", "26%", "60%", "70%", "71%"],
    "解决方案": ["2分钟报价", "Excel+VBA+Python", "PRA自动填充", "轻量化工具", "AI数字人", "服务费模式"]
})
st.dataframe(data, use_container_width=True, hide_index=True)
