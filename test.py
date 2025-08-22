import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="여성 체형별 코디 추천", page_icon="👗", layout="wide")

# 헤더
st.markdown(
    """
    <h1 style='text-align: center; color: #D81B60;'>✨ 여성 체형별 옷 코디 추천 ✨</h1>
    <p style='text-align: center; font-size:18px; color: #616161;'>
    나의 체형에 맞는 옷을 찾아서 더 세련되고 아름답게 스타일링 해보세요!
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

# 체형별 추천 데이터 (여성 스타일)
recommendations = {
    "🍎 사과형": {
        "tip": """
        - 상체(특히 배와 가슴)가 발달한 체형이에요.  
        - **허리선을 잡아주고 시선을 분산**시키는 코디가 좋아요.  
        - 어두운 색의 브이넥 블라우스, 허리가 잘록해 보이는 랩 원피스가 잘 어울려요.  
        - 하체는 A라인 스커트, 와이드 팬츠로 체형 밸런스를 맞추면 세련돼 보여요.
        """,
        "items": [
            {"name": "브이넥 블라우스 + A라인 스커트", 
             "image": "https://images.unsplash.com/photo-1602810318383-e3b8656f5a13?auto=format&fit=crop&w=600&q=80"},
            {"name": "슬림핏 랩 원피스", 
             "image": "https://images.unsplash.com/photo-1520975686519-5f8baf8c3e7d?auto=format&fit=crop&w=600&q=80"}
        ]
    },
    "🍐 배형": {
        "tip": """
        - 하체가 발달하고 골반이 넓은 체형이에요.  
        - **시선을 상체로 끌어올리는 스타일링**이 포인트!  
        - 오프숄더, 퍼프소매, 밝은 색 블라우스가 잘 어울려요.  
        - 하의는 어두운 톤의 슬림 일자핏 팬츠나 플레어 스커트 추천.
        """,
        "items": [
            {"name": "화이트 오프숄더 블라우스 + 블랙 플레어 스커트", 
             "image": "https://images.unsplash.com/photo-1519744346365-59c2f1df5d4a?auto=format&fit=crop&w=600&q=80"},
            {"name": "퍼프소매 블라우스 + 딥톤 팬츠", 
             "image": "https://images.unsplash.com/photo-1521334884684-d80222895322?auto=format&fit=crop&w=600&q=80"}
        ]
    },
    "▭ 직사각형": {
        "tip": """
        - 허리선이 잘 드러나지 않는 체형이에요.  
        - **허리를 강조하거나 볼륨감을 주는 코디**가 좋아요.  
        - 벨트, 랩 원피스, 크롭 상의 + 하이웨스트 조합이 체형을 살려줍니다.  
        """,
        "items": [
            {"name": "벨트 장식 랩 원피스", 
             "image": "https://images.unsplash.com/photo-1583225144788-7949c1c7e26a?auto=format&fit=crop&w=600&q=80"},
            {"name": "크롭 니트 + 하이웨스트 팬츠", 
             "image": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?auto=format&fit=crop&w=600&q=80"}
        ]
    },
    "⏳ 모래시계형": {
        "tip": """
        - 상체와 하체의 비율이 균형 잡힌 체형이에요.  
        - **허리를 강조하는 옷**이 가장 잘 어울려요.  
        - 슬림핏 원피스, 하이웨스트 스커트, 크롭 자켓을 활용해보세요.  
        """,
        "items": [
            {"name": "슬림핏 니트 원피스", 
             "image": "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?auto=format&fit=crop&w=600&q=80"},
            {"name": "하이웨스트 스커트 + 크롭 자켓", 
             "image": "https://images.unsplash.com/photo-1512436991641-6745cdb1723f?auto=format&fit=crop&w=600&q=80"}
        ]
    },
    "🔺 역삼각형": {
        "tip": """
        - 어깨가 넓고 상체가 발달한 체형이에요.  
        - **하체를 강조하고 상체는 심플하게** 하는 게 포인트.  
        - 베이직한 블라우스에 와이드 팬츠, 플레어 스커트가 잘 어울려요.  
        """,
        "items": [
            {"name": "심플 셔츠 + 플레어 스커트", 
             "image": "https://images.unsplash.com/photo-1520975960476-31c93cc2f3f1?auto=format&fit=crop&w=600&q=80"},
            {"name": "베이직 블라우스 + 와이드 팬츠", 
             "image": "https://images.unsplash.com/photo-1553787499-3f812472a0f3?auto=format&fit=crop&w=600&q=80"}
        ]
    }
}

# 체형 스타일링 팁 출력
st.markdown(f"### {body_shape} 스타일링 팁 💡")
st.markdown(recommendations[body_shape]["tip"])

# 오늘의 코디 버튼
st.markdown("---")
st.markdown("## 👗 오늘의 코디 추천")

if st.button(f"{body_shape} 오늘의 코디 보기 🎲"):
    outfit = random.choice(recommendations[body_shape]["items"])
    st.success(f"오늘의 코디는 👉 {outfit['name']}")
    st.image(outfit["image"], caption="세련된 오늘의 코디", use_column_width=True)
