import streamlit as st
import pandas as pd

# 页面基本设置
st.set_page_config(page_title="跌倒风险预测", page_icon="🏃‍♂️")
st.title("🏃‍♂️ 物理治疗：跌倒风险预测系统")

# 侧边栏 - 获取患者输入数据
st.sidebar.header("📋 患者数据输入")
age = st.sidebar.slider("年龄 (岁)", 50, 95, 70)
balance_score = st.sidebar.slider("平衡得分 (0-100)", 0, 100, 60)
gait_speed = st.sidebar.slider("步速 (m/s)", 0.2, 1.8, 1.0, step=0.1)
history_of_falls = st.sidebar.selectbox("过去一年跌倒次数", [0, 1, 2, 3, 4])

st.write("---")
st.subheader("📊 评估结果")

# 这里使用我们刚才演示的“模拟公式”，保证你的网页能立刻跑起来！
# 之后你只需要把这里替换成加载作业里的模型即可
risk_prob = (age/95 * 0.3) + ((100-balance_score)/100 * 0.4) + (max(0, 1.5-gait_speed)/1.5 * 0.2) + (history_of_falls/4 * 0.1)
risk_prob = min(risk_prob, 1.0) # 最高100%

# 展示结果
st.metric(label="综合跌倒风险概率", value=f"{risk_prob*100:.1f}%")

if risk_prob < 0.4:
    st.success("🟢 **低风险**：建议维持日常活动。")
elif risk_prob < 0.7:
    st.warning("🟡 **中风险**：建议物理治疗师介入，加强平衡训练。")
else:
    st.error("🔴 **高风险**：强烈建议使用助行器，开展防跌倒专项治疗！")