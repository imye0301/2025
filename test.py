import streamlit as st
import random

st.set_page_config(page_title="여성 체형별 코디 추천", page_icon="👗", layout="wide")

st.markdown(
    """
    <h1 style='text-align: center; color: #D81B60;'>✨ 여성 체형별 옷 코디 추천 ✨</h1>
    <p style='text-align: center; font-size:18px; color: #616161;'>
    나의 체형에 꼭 맞는 코디로 더 세련되고 아름답게 스타일링 해보세요!
    </p>
    """,
    unsafe_allow_html=True
)

# 체형 선택 (키와 동일하게 맞춤)
st.sidebar.header("체형을 선택하세요")
body_shape = st.sidebar.radio(
    "체형 선택",
    ["🍎 사과형", "🍐 배형", "▭ 직사각형", "⏳ 모래시계형", "🔺 역삼각형"]
)

# 딕셔너리 키도 동일하게 설정
recommendations = {
    "🍎 사과형": {
        "tip": "사과형은 상체가 발달했어요. 브이넥, 랩 원피스, A라인 스커트가 잘 어울려요.",
        "items": [
            {"name": "브이넥 블라우스 + A라인 스커트", "image": "https://..."},
            {"name": "슬림핏 랩 원피스", "image": "https://..."}
        ]
    },
    "🍐 배형": {
        "tip": "배형은 하체가 발달했어요. 밝은색 상의, 퍼프소매, 어두운색 하의가 좋아요.",
        "items": [
            {"name": "화이트 오프숄더 블라우스 + 블랙 플레어 스커트", "image": "https://..."}
        ]
    },
    "▭ 직사각형": {
        "tip": "직사각형은 허리선이 잘 안 드러나요. 벨트, 랩 원피스, 하이웨스트 아이템 추천!",
        "items": [
            {"name": "벨트 장식 랩 원피스", "image": "https://..."}
        ]
    },
    "⏳ 모래시계형": {
        "tip": "모래시계형은 허리를 강조하는 옷이 잘 어울려요.",
        "items": [
            {"name": "슬림핏 니트 원피스", "image": "https://..."}
        ]
    },
    "🔺 역삼각형": {
        "tip": "역삼각형은 하체 강조, 상체는 심플하게!",
        "items": [
            {"name": "심플 셔츠 + 플레어 스커트", "image": "https://..."}
        ]
    }
}

# 스타일링 팁 출력
st.markdown(f"### {body_shape} 스타일링 팁")
st.markdown(recommendations[body_shape]["tip"])

# 오늘의 코디 버튼
st.markdown("---")
st.markdown("## 오늘의 코디 추천")

if st.button(f"{body_shape} 오늘의 코디 보기 🎲"):
    outfit = random.choice(recommendations[body_shape]["items"])
    st.success(f"오늘의 추천 코디: **{outfit['name']}**")
    st.image(outfit["image"], caption="세련된 코디 예시", use_column_width=True)
