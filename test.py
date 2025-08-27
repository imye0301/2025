import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="체형별 옷 코디 가이드", layout="centered")

# 사용자 정의 CSS 추가 (파스텔톤 배경 + 화려한 스타일)
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
}

h1 {
    font-family: 'Comic Sans MS', 'Arial Rounded MT Bold', cursive, sans-serif;
    font-weight: bold;
    color: #444444;
    text-shadow: 2px 2px 8px #ffffffaa;
}

.stInfo, .stSuccess {
    border-radius: 12px;
    font-size: 18px;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# 제목
st.title("👗 체형별 옷 코디 가이드")
st.write("당신의 체형에 맞는 패션 코디 팁을 확인해보세요!")

# 체형 선택 옵션
types = [
    "사과형 🍎 (상체가 발달한 체형)",
    "배형 🍐 (하체가 발달한 체형)",
    "직사각형 ▭ (허리라인이 잘 안 보이는 체형)",
    "모래시계형 ⏳ (균형잡힌 체형)",
    "역삼각형 🔻 (어깨가 넓은 체형)"
]

choice = st.selectbox("당신의 체형을 선택하세요:", types)

# 체형별 코디 추천 데이터 + 색감 테마
tips = {
    "사과형 🍎 (상체가 발달한 체형)": ("상체는 심플하게, 하체에 포인트를 주는 것이 좋아요. A라인 스커트, 와이드 팬츠 추천!", "#FFB6B9"),
    "배형 🍐 (하체가 발달한 체형)": ("밝은 톤 상의 + 어두운 톤 하의로 시선을 위로 끌어올리세요. 화려한 액세서리도 효과적!", "#FFDCA2"),
    "직사각형 ▭ (허리라인이 잘 안 보이는 체형)": ("허리를 강조하는 벨트, 하이웨이스트 팬츠, 크롭탑 스타일링 추천!", "#A0E7E5"),
    "모래시계형 ⏳ (균형잡힌 체형)": ("몸의 라인을 살려주는 원피스, 슬림핏 의상이 잘 어울립니다. 대부분의 스타일 소화 가능!", "#B4F8C8"),
    "역삼각형 🔻 (어깨가 넓은 체형)": ("브이넥 상의로 어깨를 좁아보이게, 플레어 스커트나 부츠컷 바지로 하체 볼륨감을 주세요.", "#C8B6FF")
}

# 결과 출력
st.subheader("추천 코디")

message, color = tips[choice]
st.markdown(
    f"""
    <div style='background-color:{color}; padding:20px; border-radius:20px; color:#333333; font-size:18px; font-weight:bold; box-shadow: 4px 4px 15px #00000033;'>
        {message}
    </div>
    """,
    unsafe_allow_html=True
)

# 예시 이미지 출력 (임시 예시 URL)
if choice == "사과형 🍎 (상체가 발달한 체형)":
    st.image("https://i.imgur.com/3dM0t7M.jpg", caption="사과형 코디 예시", use_container_width=True)
elif choice == "배형 🍐 (하체가 발달한 체형)":
    st.image("https://i.imgur.com/sbVVQox.jpg", caption="배형 코디 예시", use_container_width=True)
elif choice == "직사각형 ▭ (허리라인이 잘 안 보이는 체형)":
    st.image("https://i.imgur.com/EDuOy1c.jpg", caption="직사각형 코디 예시", use_container_width=True)
elif choice == "모래시계형 ⏳ (균형잡힌 체형)":
    st.image("https://i.imgur.com/CSv0Wdo.jpg", caption="모래시계형 코디 예시", use_container_width=True)
elif choice == "역삼각형 🔻 (어깨가 넓은 체형)":
    st.image("https://i.imgur.com/qwB8Zm6.jpg", caption="역삼각형 코디 예시", use_container_width=True)

st.success("체형에 맞는 코디로 자신감을 표현해보세요! ✨")
