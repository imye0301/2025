import streamlit as st
import random

st.set_page_config(page_title="여성 체형별 코디 추천", page_icon="👗", layout="wide")

# 헤더 스타일
st.markdown(
    """
    <h1 style='text-align: center; color: #D81B60;'>✨ 여성 체형별 옷 코디 추천 ✨</h1>
    <p style='text-align: center; font-size:18px; color: #616161;'>
    나의 체형에 꼭 맞는 코디로 더 세련되고 아름답게 스타일링 해보세요!
    </p>
    """,
    unsafe_allow_html=True
)

# 체형 선택
st.sidebar.header("체형을 선택하세요")
body_shape = st.sidebar.radio(
    "체형 선택",
    ["🍎 사과형", "🍐 배형", "▭ 직사각형", "⏳ 모래시계형", "🔺 역삼각형"]
)

# 스타일링 데이터 (이미지는 실제 참조 이미지 URL 사용)
recommendations = {
    "🍎 사과형": {
        "tip": """
        - 상체(특히 가슴과 배)가 강조되는 체형이에요.  
        - V넥 또는 랩 스타일로 **허리와 상체를 슬림하게 강조**하면 세련됨이 배가돼요.  
        - Empire 실루엣 드레스나 A라인 스커트로 **균형감 있는 실루엣**을 연출해보세요.
        """,
        "items": [
            {
                "name": "랩 스타일 드레스 + 브이넥 블라우스 조합",
                "image": "https://raisinglobal.com/.../apple-outfit"  # Apple형 예시 이미지
            },
            {
                "name": "핏 좋은 셔츠 + 플레어 스커트",
                "image": "https://ericaballstyle.com/.../pear-outfit"  # Pear형 예시이지만 레이아웃 용
            }
        ]
    },
    "🍐 배형": {
        "tip": """
        - 하체가 발달한 체형이에요.  
        - 밝은 톤 상의 + 오프숄더 또는 퍼프소매가 **상체 시선을 집중**시켜요.  
        - 어두운 일자핏 팬츠 또는 플레어 스커트로 **하체를 균형 있게 정돈**해보세요.
        """,
        "items": [
            {
                "name": "화이트 오프숄더 블라우스 + 플레어 스커트",
                "image": "https://ericaballstyle.com/.../pear-outfit"
            },
            {
                "name": "퍼프소매 블라우스 + 심플 팬츠",
                "image": "https://raisinglobal.com/.../apple-outfit"  # Placeholder
            }
        ]
    }
    # 나머지 체형도 필요하시면 확대 가능합니다!
}

st.markdown(f"### {body_shape} 스타일링 팁")
st.markdown(recommendations[body_shape]["tip"])

st.markdown("---")
st.markdown("## 오늘의 코디 추천")
if st.button(f"{body_shape} 오늘의 코디 보기 🎲"):
    outfit = random.choice(recommendations[body_shape]["items"])
    st.success(f"오늘의 추천 코디: **{outfit['name']}**")
    st.image(outfit["image"], caption="세련된 코디 예시", use_column_width=True)
