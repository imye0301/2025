import streamlit as st
import random

st.set_page_config(page_title="체형별 코디 추천", page_icon="👗", layout="wide")

st.title("👗 체형별 옷 코디 추천 웹앱")

# 체형별 추천 데이터
recommendations = {
    "사과형 🍎": {
        "tip": """
        - 상체가 발달해 배 부분이 두드러지는 체형이에요.  
        - **허리선을 강조하거나 시선을 분산**시키는 스타일이 좋아요.  
        - 상의는 V넥, 랩 스타일, 어두운 색 계열을 선택하세요.  
        - 하의는 A라인 스커트, 와이드 팬츠처럼 체형 밸런스를 맞춰주는 아이템이 잘 어울려요.  
        """,
        "items": [
            {"name": "V넥 블라우스 + A라인 스커트", 
             "image": "https://images.unsplash.com/photo-1602810318383-e3b8656f5a13?auto=format&fit=crop&w=500&q=80"},
            {"name": "랩 원피스", 
             "image": "https://images.unsplash.com/photo-1520975686519-5f8baf8c3e7d?auto=format&fit=crop&w=500&q=80"}
        ]
    },
    "배형 🍐": {
        "tip": """
        - 하체가 발달한 체형이에요.  
        - **시선을 상체로 끌어올리는 스타일링**이 포인트예요.  
        - 밝은색이나 패턴 있는 상의, 퍼프소매, 오프숄더가 잘 어울려요.  
        - 하의는 어두운색 계열의 일자핏 바지나 플레어 스커트를 추천해요.  
        """,
        "items": [
            {"name": "오프숄더 블라우스 + 플레어 스커트", 
             "image": "https://images.unsplash.com/photo-1519744346365-59c2f1df5d4a?auto=format&fit=crop&w=500&q=80"},
            {"name": "퍼프소매 상의 + 일자핏 팬츠", 
             "image": "https://images.unsplash.com/photo-1521334884684-d80222895322?auto=format&fit=crop&w=500&q=80"}
        ]
    },
    "직사각형 ▭": {
        "tip": """
        - 허리 라인이 잘 드러나지 않는 체형이에요.  
        - **허리를 강조하거나 볼륨감을 주는 코디**가 좋아요.  
        - 벨트, 랩 원피스, 크롭 상의 등으로 허리선을 잡아주세요.  
        - 패턴이나 디테일이 들어간 옷으로 시각적인 변화를 주는 것도 효과적이에요.  
        """,
        "items": [
            {"name": "벨트 랩 원피스", 
             "image": "https://images.unsplash.com/photo-1583225144788-7949c1c7e26a?auto=format&fit=crop&w=500&q=80"},
            {"name": "크롭 상의 + 하이웨스트 팬츠", 
             "image": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?auto=format&fit=crop&w=500&q=80"}
        ]
    },
    "모래시계형 ⏳": {
        "tip": """
        - 상체와 하체의 균형이 좋은 체형이에요.  
        - **허리를 강조하는 스타일링**이 잘 어울려요.  
        - 슬림핏 원피스, 하이웨스트 스커트, 크롭 자켓 등이 체형을 돋보이게 해요.  
        """,
        "items": [
            {"name": "슬림핏 원피스", 
             "image": "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?auto=format&fit=crop&w=500&q=80"},
            {"name": "하이웨스트 스커트 + 크롭 자켓", 
             "image": "https://images.unsplash.com/photo-1512436991641-6745cdb1723f?auto=format&fit=crop&w=500&q=80"}
        ]
    },
    "역삼각형 🔺": {
        "tip": """
        - 어깨가 넓고 상체가 발달한 체형이에요.  
        - **하체를 강조하고 상체는 심플하게** 연출하는 것이 좋아요.  
        - 와이드 팬츠, 플레어 스커트, 밝은색 하의가 어울려요.  
        - 상체는 단색 계열의 심플한 디자인으로 맞춰주세요.  
        """,
        "items": [
            {"name": "심플한 블라우스 + 와이드 팬츠", 
             "image": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA3MjFfMjA4%2FMDAxNjg5OTE5MTMyNTg5.qbrws0rxWYJu5HW_tHhgiJM7tjqiQdFH7KDJh_gDzAgg.4YJVqMaIqcixlR6CDsA5bU6WwEBh5glAdnbrcL06e6Ug.PNG.fmmn3125%2F5.png&type=a340"},
            {"name": "베이직 셔츠 + 플레어 스커트", 
             "image": "https://images.unsplash.com/photo-1520975960476-31c93cc2f3f1?auto=format&fit=crop&w=500&q=80"}
        ]
    }
}

# ✅ 버튼으로 체형 선택
st.subheader("체형을 선택하세요")
cols = st.columns(5)
body_shape = None
shapes = list(recommendations.keys())

for i, col in enumerate(cols):
    if col.button(shapes[i]):
        body_shape = shapes[i]

# 선택된 체형 있을 때만 표시
if body_shape:
    st.subheader(f"{body_shape} 스타일링 팁 ✨")
    st.markdown(recommendations[body_shape]["tip"])

    st.subheader("👗 오늘의 코디 추천")
    if st.button(f"{body_shape} 오늘의 코디 뽑기 🎲"):
        outfit = random.choice(recommendations[body_shape]["items"])
        st.success(f"오늘의 추천 코디 👉 {outfit['name']}")

        # 모든 코디 보여주기
        for item in recommendations[body_shape]["items"]:
            if item["name"] == outfit["name"]:
                st.image(item["image"], caption=f"⭐ {item['name']} (추천)", use_column_width=True)
            else:
                st.image(item["image"], caption=item["name"], use_column_width=True)
