import streamlit as st
import random

st.set_page_config(page_title="체형별 코디 추천", page_icon="👗", layout="wide")

st.title("👗 체형별 옷 코디 추천 웹앱")

# 체형 선택
st.sidebar.header("체형을 선택하세요")
body_shape = st.sidebar.selectbox(
    "체형",
    ["사과형 🍎", "배형 🍐", "직사각형 ▭", "모래시계형 ⏳", "역삼각형 🔺"]
)

# 체형별 추천 데이터
recommendations = {
    "사과형 🍎": {
        "tip": "상체가 발달한 체형이에요. 허리선을 살려주는 A라인 원피스나 V넥 상의가 좋아요.",
        "items": ["A라인 원피스", "V넥 블라우스", "하이웨스트 팬츠"],
        "image": "https://images.unsplash.com/photo-1602810318383-e3b8656f5a13?auto=format&fit=crop&w=400&q=80"
    },
    "배형 🍐": {
        "tip": "하체가 발달한 체형이에요. 상체를 강조하는 오프숄더, 퍼프 블라우스가 잘 어울려요.",
        "items": ["오프숄더 블라우스", "플레어 스커트", "밝은색 상의"],
        "image": "https://images.unsplash.com/photo-1519744346365-59c2f1df5d4a?auto=format&fit=crop&w=400&q=80"
    },
    "직사각형 ▭": {
        "tip": "허리선이 잘 안 드러나는 체형이에요. 벨트를 활용해 허리를 강조하면 좋아요.",
        "items": ["랩 원피스", "벨트 코디", "패턴 상의"],
        "image": "https://images.unsplash.com/photo-1520975686519-5f8baf8c3e7d?auto=format&fit=crop&w=400&q=80"
    },
    "모래시계형 ⏳": {
        "tip": "체형 밸런스가 좋은 편이에요. 허리를 강조하는 옷이 잘 어울려요.",
        "items": ["슬림핏 드레스", "하이웨스트 스커트", "크롭 자켓"],
        "image": "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?auto=format&fit=crop&w=400&q=80"
    },
    "역삼각형 🔺": {
        "tip": "어깨가 넓은 체형이에요. 하체를 강조하는 와이드 팬츠, 플레어 스커트가 좋아요.",
        "items": ["와이드 팬츠", "플레어 스커트", "밝은색 하의"],
        "image": "https://images.unsplash.com/photo-1553787499-3f812472a0f3?auto=format&fit=crop&w=400&q=80"
    }
}

# 현재 선택된 체형 추천
st.subheader(f"{body_shape} 코디 추천 ✨")
st.write(recommendations[body_shape]["tip"])
st.write("**추천 아이템:**")
for item in recommendations[body_shape]["items"]:
    st.markdown(f"- {item}")

st.image(recommendations[body_shape]["image"], caption="코디 예시", use_column_width=True)

# 오늘의 랜덤 코디 추천
st.markdown("---")
st.subheader("🎲 오늘의 코디 랜덤 추천")

if st.button("랜덤 코디 뽑기"):
    random_shape = random.choice(list(recommendations.keys()))
    rec = recommendations[random_shape]
    
    st.success(f"오늘의 코디는 👉 {random_shape}")
    st.write(rec["tip"])
    st.write("**추천 아이템:**")
    for item in rec["items"]:
        st.markdown(f"- {item}")
    st.image(rec["image"], caption="랜덤 코디 예시", use_column_width=True)
