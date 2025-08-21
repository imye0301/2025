import streamlit as st

st.set_page_config(page_title="🌟 MBTI 진로 탐색 🌟", layout="wide")

# 🎉 타이틀 & 소개
st.markdown("""
# 🌈✨ MBTI 기반 진로 탐색 사이트 ✨🌈
당신의 성격 유형에 맞는 **꿈의 직업**을 찾아보세요! 🚀🔥  
""")

st.markdown("---")

# 🎭 MBTI 선택
mbti = st.selectbox(
    "🔮 당신의 MBTI를 선택하세요:",
    ["INTJ 🧠", "ENTP 🎤", "INFJ 🌌", "ESFP 🎉", "ISTP 🔧", "ENFP 🌈", 
     "ISTJ 📊", "ESTJ 💼", "INFP 🎨", "ENTJ 👑", "ISFJ 🤝", "ESFJ 🕊️", 
     "ISFP 🌿", "ENFJ 🌟", "ESTP ⚡", "INTP 🤓"]
)

# 🎨 데이터베이스 (간단 예시)
career_dict = {
    "INTJ 🧠": ["전략기획가 📈", "데이터 분석가 💻", "연구원 🔬"],
    "ENFP 🌈": ["마케터 📣", "크리에이터 🎬", "심리상담가 🧩"],
    "ISTJ 📊": ["회계사 💰", "공무원 🏛️", "엔지니어 ⚙️"],
    "ESFP 🎉": ["배우 🎭", "MC 🎤", "여행가이드 ✈️"],
}

# 🎁 결과 출력
st.markdown(f"## 🎯 당신의 MBTI는: **{mbti}** ✨")

if mbti in career_dict:
    st.markdown("### 🌟 어울리는 직업 추천 🌟")
    for job in career_dict[mbti]:
        st.markdown(f"- {job}")
else:
    st.warning("🚧 해당 MBTI에 대한 데이터가 준비 중입니다 🛠️")

# 🌍 추가 자료 (예시)
st.markdown("---")
st.markdown("## 📚 더 알아보기")
col1, col2, col3 = st.columns(3)

with col1:
    st.success("💡 **성격 강점**\n- 리더십 🦁\n- 창의성 🎨\n- 집중력 🎯")

with col2:
    st.info("⚠️ **주의할 점**\n- 완벽주의 🌀\n- 고집 🙅\n- 과한 열정 🔥")

with col3:
    st.error("🌟 **유명인 사례**\n- 엘론 머스크 🚀\n- 오프라 윈프리 🎤\n- BTS RM 🎶")

# 🎉 하단 메시지
st.markdown("---")
st.markdown("## 🌟 오늘부터 당신의 진로 여정을 시작하세요! 🚀🔥✨")
st.balloons()
