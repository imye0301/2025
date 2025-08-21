import streamlit as st

st.set_page_config(page_title="MBTI 진로 탐색", layout="wide")

st.title("🔮 MBTI 기반 진로 탐색 사이트")

# MBTI 선택
mbti = st.selectbox("당신의 MBTI를 선택하세요:", 
                    ["INTJ", "ENTP", "INFJ", "ESFP", "ISTP", "ENFP", "ISTJ", "ESTJ", 
                     "INFP", "ENTJ", "ISFJ", "ESFJ", "ISFP", "ENFJ", "ESTP", "INTP"])

st.write(f"당신의 MBTI는 **{mbti}** 입니다!")

# MBTI별 진로 추천 데이터 (간단 예시)
career_dict = {
    "INTJ": ["전략기획가", "데이터 분석가", "연구원"],
    "ENFP": ["마케터", "크리에이터", "심리상담가"],
    "ISTJ": ["회계사", "공무원", "엔지니어"],
    "ESFP": ["배우", "MC", "여행가이드"]
}

if mbti in career_dict:
    st.subheader("추천 진로")
    for job in career_dict[mbti]:
        st.markdown(f"- {job}")
else:
    st.warning("해당 MBTI에 대한 데이터가 아직 준비되지 않았습니다.")
