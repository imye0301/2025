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
st.title("👗 아침마다 고민하지 말고 코디 추천 받자!")
st.write("당신의 체형에 맞는 패션 코디 팁과 추천 아이템을 확인해보세요!")

# 체형 선택 옵션
types = [
    "사과형 🍎 (상체가 발달한 체형)",
    "배형 🍐 (하체가 발달한 체형)",
    "직사각형 ▭ (허리라인이 잘 안 보이는 체형)",
    "모래시계형 ⏳ (균형잡힌 체형)",
    "역삼각형 🔻 (어깨가 넓은 체형)"
]

choice = st.selectbox("당신의 체형을 선택하세요:", types)

# 체형별 코디 추천 데이터 + 색감 테마 + 아이템 + 브랜드
tips = {
    "사과형 🍎 (상체가 발달한 체형)": {
        "message": "상체는 심플하게, 하체에 포인트를 주는 것이 좋아요. A라인 스커트, 와이드 팬츠 추천!",
        "color": "#FFB6B9",
        "items": {
            "👕 상의": ("심플한 블라우스, 브이넥 티셔츠", ["무신사", "ZARA"]),
            "👖 하의": ("플레어 스커트, 와이드 팬츠", ["H&M", "COS"]),
            "👟 신발": ("로퍼, 슬링백 힐", ["구두샵", "CHARLES & KEITH"]),
            "💍 액세서리": ("롱 네크리스, 심플 이어링", ["OST", "SWAROVSKI"])
        }
    },
    "배형 🍐 (하체가 발달한 체형)": {
        "message": "밝은 톤 상의 + 어두운 톤 하의로 시선을 위로 끌어올리세요. 화려한 액세서리도 효과적!",
        "color": "#FFDCA2",
        "items": {
            "👕 상의": ("밝은 톤 블라우스, 셔츠", ["ZARA", "8seconds"]),
            "👖 하의": ("블랙 슬랙스, 어두운 스커트", ["H&M", "유니클로"]),
            "👟 신발": ("굽 있는 샌들, 웨지힐", ["ALDO", "슈콤마보니"]),
            "💍 액세서리": ("스테이트먼트 귀걸이, 볼드 목걸이", ["앤아더스토리즈", "SWAROVSKI"])
        }
    },
    "직사각형 ▭ (허리라인이 잘 안 보이는 체형)": {
        "message": "허리를 강조하는 벨트, 하이웨이스트 팬츠, 크롭탑 스타일링 추천!",
        "color": "#A0E7E5",
        "items": {
            "👕 상의": ("크롭탑, 셔츠", ["Stylenanda", "무신사"]),
            "👖 하의": ("하이웨이스트 팬츠, 벨트 스커트", ["ZARA", "H&M"]),
            "👟 신발": ("스니커즈, 앵클부츠", ["CONVERSE", "Dr.Martens"]),
            "💍 액세서리": ("와이드 벨트, 브레이슬릿", ["COS", "앤아더스토리즈"])
        }
    },
    "모래시계형 ⏳ (균형잡힌 체형)": {
        "message": "몸의 라인을 살려주는 원피스, 슬림핏 의상이 잘 어울립니다. 대부분의 스타일 소화 가능!",
        "color": "#B4F8C8",
        "items": {
            "👕 상의": ("슬림핏 블라우스, 니트", ["ZARA", "H&M"]),
            "👖 하의": ("펜슬 스커트, 슬림진", ["COS", "무신사"]),
            "👟 신발": ("하이힐, 앵클부츠", ["Jimmy Choo", "슈콤마보니"]),
            "💍 액세서리": ("골드 네크리스, 우아한 귀걸이", ["SWAROVSKI", "Pandora"])
        }
    },
    "역삼각형 🔻 (어깨가 넓은 체형)": {
        "message": "브이넥 상의로 어깨를 좁아보이게, 플레어 스커트나 부츠컷 바지로 하체 볼륨감을 주세요.",
        "color": "#C8B6FF",
        "items": {
            "👕 상의": ("브이넥 블라우스, 오프숄더", ["ZARA", "무신사"]),
            "👖 하의": ("플레어 스커트, 부츠컷 팬츠", ["H&M", "8seconds"]),
            "👟 신발": ("굽 있는 샌들, 펌프스", ["CHARLES & KEITH", "슈콤마보니"]),
            "💍 액세서리": ("드롭 귀걸이, 브레이슬릿", ["OST", "앤아더스토리즈"])
        }
    }
}

# 결과 출력
st.subheader("추천 코디")

message = tips[choice]["message"]
color = tips[choice]["color"]
items = tips[choice]["items"]

st.markdown(
    f"""
    <div style='background-color:{color}; padding:20px; border-radius:20px; color:#333333; font-size:18px; font-weight:bold; box-shadow: 4px 4px 15px #00000033;'>
        {message}
    </div>
    """,
    unsafe_allow_html=True
)

# 추천 아이템 카드
st.subheader("✨ 추천 아이템 & 브랜드")
for icon, (text, brands) in items.items():
    brand_list = " / ".join(brands)
    st.markdown(
        f"""
        <div style='background:#ffffffdd; margin:10px 0; padding:12px; border-radius:15px; font-size:16px; box-shadow: 2px 2px 8px #00000022;'>
            <b>{icon}</b> : {text}<br>
            <span style='color:#666; font-size:14px;'>추천 브랜드 👉 {brand_list}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# 예시 이미지 출력 (임시 예시 URL)
if choice == "사과형 🍎 (상체가 발달한 체형)":
    st.image("https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNTA2MTlfMjkg%2FMDAxNzUwMjcxMTA3ODQ1.vYIfTu2Ky-Pg_KHU-PV7rIPHWtZP_kfhSkBwzxL0mMwg.zQ6whAtGJeFsBrXq5vPuw3cqNSrZAMCsGi64gyKgFYQg.JPEG%2F%25B3%25D7%25C0%25CC%25BA%25F1%252B%25C8%25AD%25C0%25CC%25C6%25AE.jpg&type=a340", caption="사과형 코디 예시", use_container_width=True)
elif choice == "배형 🍐 (하체가 발달한 체형)":
    st.image("https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNTA2MTlfNDAg%2FMDAxNzUwMzIxMzQ1MDAy.ffNp8BDxomNCi2E0w46n3aemHhDZ2JuAbUwefMAkwKcg.4NUaOuW6yIJPGY8oOR_kPgqrThNn_q3ybRftMmO4Wckg.JPEG%2F%25C7%25CF%25C3%25BC%25BA%25F1%25B8%25B8%25C4%25DA%25B5%25F0.jpg&type=a340//ihttps.imgur.com/sbVVQox.jpg", caption="배형 코디 예시", use_container_width=True)
elif choice == "직사각형 ▭ (허리라인이 잘 안 보이는 체형)":
    st.image("https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNTA1MDNfMjY1%2FMDAxNzQ2Mjc3MDgzODMz.Oz-UPyyvA5MlZRY_UpE2RnkJmXGbO13O0ko3ixL8GEog.OfyCGITNBqW1fzuXrfipucwbibdDF2fpnkzN2tX_3Tgg.JPEG%2F1746268796777.jpg&type=sc960_832", caption="직사각형 코디 예시", use_container_width=True)
elif choice == "모래시계형 ⏳ (균형잡힌 체형)":
    st.image("https://search.pstatic.net/sunny/?src=https%3A%2F%2Fi3.codibook.net%2Ffiles%2F1979030444474%2F73981c75fb35dbcf%2F380362269.jpg&type=sc960_832", caption="모래시계형 코디 예시", use_container_width=True)
elif choice == "역삼각형 🔻 (어깨가 넓은 체형)":
    st.image("https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20150409_84%2Fmusecloset_1428542926799iHJBE_JPEG%2F2d80d08aa418d046ba1c7a58899ec44f.jpg&type=sc960_832", caption="역삼각형 코디 예시", use_container_width=True)

st.success("체형에 맞는 코디로 자신감을 표현해보세요! ✨")
