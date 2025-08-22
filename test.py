import streamlit as st
import random

st.set_page_config(page_title="여성 체형별 코디 추천", page_icon="👗", layout="wide")

# 헤더
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

# 체형별 추천 데이터 (실제 예시 이미지)
recommendations = {
    "🍎 사과형": {
        "tip": """
        - 상체, 특히 복부와 가슴이 발달한 체형이에요.  
        - **허리를 잘록하게 보이게 하는 브이넥/랩 스타일**이 잘 어울려요.  
        - 하체는 A라인 스커트, 와이드 팬츠로 시선을 분산시키면 더욱 세련돼 보여요.
        """,
        "items": [
            {
                "name": "랩 스타일 원피스",
                "image": "https://40plusstyle.com/wp-content/uploads/2020/08/Apple-body-shape-outfit-ideas.jpg"
            },
            {
                "name": "브이넥 블라우스 + A라인 스커트",
                "image": "https://raisinglobal.com/cdn/shop/articles/apple_body_shape_outfits.jpg"
            }
        ]
    },
    "🍐 배형": {
        "tip": """
        - 골반과 허벅지가 발달한 체형이에요.  
        - **상체에 시선을 모으는 오프숄더, 퍼프소매, 밝은 톤 상의**가 잘 어울려요.  
        - 하체는 어두운 톤의 일자핏 팬츠나 플레어 스커트를 추천해요.
        """,
        "items": [
            {
                "name": "화이트 오프숄더 블라우스 + 블랙 플레어 스커트",
                "image": "https://ericaballstyle.com/wp-content/uploads/2022/04/pear-shaped-outfits.jpg"
            },
            {
                "name": "퍼프소매 블라우스 + 딥톤 팬츠",
                "image": "https://i0.wp.com/www.collegefashion.net/wp-content/uploads/2021/07/outfits-for-pear-body-shape.jpg"
            }
        ]
    },
    "▭ 직사각형": {
        "tip": """
        - 허리선이 잘 드러나지 않는 체형이에요.  
        - **벨트, 랩 원피스, 크롭 상의 + 하이웨스트** 조합이 체형을 보완해줘요.  
        """,
        "items": [
            {
                "name": "벨트 장식 랩 원피스",
                "image": "https://40plusstyle.com/wp-content/uploads/2018/04/Rectangle-body-shape-dresses.jpg"
            },
            {
                "name": "크롭 니트 + 하이웨스트 팬츠",
                "image": "https://i.pinimg.com/564x/f6/dc/20/f6dc20.jpg"
            }
        ]
    },
    "⏳ 모래시계형": {
        "tip": """
        - 상체와 하체가 균형 잡힌 체형이에요.  
        - **허리를 강조하는 코디**가 잘 어울려요.  
        - 슬림핏 드레스, 하이웨스트 스커트, 크롭 자켓을 추천합니다.  
        """,
        "items": [
            {
                "name": "슬림핏 니트 원피스",
                "image": "https://40plusstyle.com/wp-content/uploads/2018/04/hourglass-body-shape-dresses.jpg"
            },
            {
                "name": "하이웨스트 스커트 + 크롭 자켓",
                "image": "https://i.pinimg.com/564x/45/4d/aa/454daa.jpg"
            }
        ]
    },
    "🔺 역삼각형": {
        "tip": """
        - 어깨가 넓고 상체가 발달한 체형이에요.  
        - **하체를 강조하고 상체는 심플하게** 코디하는 것이 좋아요.  
        - 와이드 팬츠, 플레어 스커트와 잘 어울립니다.
        """,
        "items": [
            {
                "name": "심플 블라우스 + 플레어 스커트",
                "image": "https://40plusstyle.com/wp-content/uploads/2021/05/inverted-triangle-body-shape-outfits.jpg"
            },
            {
                "name": "베이직 셔츠 + 와이드 팬츠",
                "image": "https://i.pinimg.com/564x/d2/d8/ff/d2d8ff.jpg"
            }
        ]
    }
}

# 선택된 체형 팁 출력
st.markdown(f"### {body_shape} 스타일링 팁 💡")
st.markdown(recommendations[body_shape]["tip"])

# 오늘의 코디 버튼
st.markdown("---")
st.markdown("## 👗 오늘의 코디 추천")

if st.button(f"{body_shape} 오늘의 코디 보기 🎲"):
    outfit = random.choice(recommendations[body_shape]["items"])
    st.success(f"오늘의 추천 코디: **{outfit['name']}**")
    st.image(outfit["image"], caption="세련된 코디 예시", use_column_width=True)
