import streamlit as st
import random

st.set_page_config(page_title="여성 체형별 데일리 코디 추천", page_icon="👗", layout="wide")

# CSS 스타일 (배경색 + 카드 스타일 + 버튼 효과)
st.markdown("""
    <style>
    body {
        background-color: #E3F2FD; /* 연한 파랑 배경 */
    }
    [data-testid="stAppViewContainer"] {
        background-color: #E3F2FD;
    }
    [data-testid="stSidebar"] {
        background-color: #BBDEFB; /* 사이드바 연한 블루 */
    }
    h1, h2, h3 {
        color: #1565C0; /* 진한 파랑 포인트 */
    }
    .stButton>button {
        background: linear-gradient(to right, #42A5F5, #1E88E5);
        color: white;
        border-radius: 12px;
        padding: 0.6em 1.2em;
        font-size: 16px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(to right, #64B5F6, #1976D2);
        transform: scale(1.05);
    }
    .stSuccess {
        background-color: #BBDEFB;
        color: #0D47A1;
        border-radius: 10px;
        padding: 10px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 헤더
st.markdown(
    """
    <h1 style='text-align: center;'>
        👗 나에게 꼭 맞는 데일리 코디
    </h1>
    <p style='text-align: center; font-size:18px; color: #424242;'>
        체형별 실생활 패션 예시를 참고해서 세련되고 화려한 코디를 즐겨보세요! ✨
    </p>
    """,
    unsafe_allow_html=True
)

# 체형 선택
st.sidebar.header("체형을 선택하세요")
body_shape = st.sidebar.radio(
    "체형 선택",
    ["🍎 Apple형", "🍐 Pear형"]
)

# 추천 데이터
recommendations = {
    "🍎 Apple형": {
        "tip": """
        - 상체 중심 체형 → V넥, 랩 스타일 상의 추천  
        - 허리 강조보다 자연스러운 실루엣이 예뻐요  
        - 브이넥 + 하이웨이스트 하의는 세련된 데일리룩 완성!
        """,
        "items": [
            {
                "name": "브이넥 상의 + 하이웨이스트 팬츠 (데일리)",
                "image": "https://raisinglobal.com/blogs/news/best-outfits-for-apple-shaped-body-in-2024"
            },
            {
                "name": "랩 원피스 스타일 – 스트릿 패션",
                "image": "https://ericaballstyle.com/how-to-dress-an-apple-body-type/"
            }
        ]
    },
    "🍐 Pear형": {
        "tip": """
        - 하체 중심 체형 → 상체 포인트 코디 추천  
        - 오프숄더, 퍼프소매, 밝은 컬러 상의 활용  
        - 하의는 깔끔한 톤의 팬츠나 스커트가 조화로워요
        """,
        "items": [
            {
                "name": "밝은 블라우스 + 심플 데님",
                "image": "https://ericaballstyle.com/how-to-style-a-pear-shaped-body-type/"
            }
        ]
    }
}

# 설명 출력
st.markdown(f"### {body_shape} 스타일링 팁 💡")
st.markdown(recommendations[body_shape]["tip"])

# 오늘의 코디 추천
st.markdown("---")
st.markdown("## 🎲 오늘의 데일리 코디 추천")

if st.button(f"{body_shape} 코디 보기"):
    outfit = random.choice(recommendations[body_shape]["items"])
    st.success(f"✨ 오늘의 추천 코디: **{outfit['name']}** ✨")
    st.image(outfit["image"], caption="실생활 감각 코디", use_column_width=True)
