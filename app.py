
import streamlit as st

# ==========================================
# 체대입시생 실기가이드 & 보강운동 추천 앱
# 고려대학교 2026학년도 공개 기준 참고
# ==========================================

st.set_page_config(
    page_title="체대입시 실기가이드",
    page_icon="🏃",
    layout="centered"
)

# ------------------------------------------
# 1. 앱 제목
# ------------------------------------------

st.title("🏃 체대입시 실기가이드")
st.subheader("나의 실기 기록 분석 & 맞춤형 보강운동")

st.write(
    "성별과 실기 종목을 선택하고 기록을 입력하면 "
    "실기 점수와 맞춤형 보강운동을 확인할 수 있습니다."
)

st.info(
    "고려대학교 2026학년도 공개 실기 기준 참고 프로그램입니다. "
    "각 종목은 서로 다른 모집단위의 기준을 사용합니다."
)

st.divider()


# ------------------------------------------
# 2. 실기 기준표 (리스트)
# ------------------------------------------

# 고려대 세종 국제스포츠학부 2026 기준
score_list = [
    133, 130, 127, 124, 121,
    118, 115, 112, 109, 106,
    103, 100, 97, 94, 91,
    88, 85, 82, 79, 76,
    73, 70, 67, 64, 61
]

# 10m 왕복달리기 기준
run_male = [
    round(8.50 + 0.10 * i, 2)
    for i in range(24)
]

run_female = [
    round(9.50 + 0.10 * i, 2)
    for i in range(24)
]

# 제자리 멀리뛰기 기준
jump_male = [
    300 - 3 * i for i in range(24)
]

jump_female = [
    250 - 3 * i for i in range(24)
]

# 고려대 서울 체육교육과 2026 높이뛰기 기준
height_male = [
    162, 160, 158, 156, 154, 152, 150,
    148, 146, 144, 142, 140
]

height_female = [
    130, 128, 126, 124, 122, 120, 118,
    116, 114, 112, 110, 108
]

height_scores = [
    100, 99, 98, 97, 96, 95, 94,
    93, 92, 85, 78, 71
]

height_grades = [
    "A+", "A", "A-", "B+", "B", "B-",
    "C+", "C", "C-", "D+", "D", "D-"
]


# ------------------------------------------
# 3. 보강운동 자료 (딕셔너리와 리스트)
# ------------------------------------------

exercise_list = {

    "10m 왕복달리기": [
        ["사이드 스텝", "10회 x 2세트", "주 2회"],
        ["스쿼트", "10회 x 2세트", "주 2회"],
        ["방향 전환 연습", "5회 x 2세트", "주 2회"],
        ["짧은 가속 달리기", "10m x 3회", "주 2회"]
    ],

    "제자리 멀리뛰기": [
        ["스쿼트", "10회 x 2세트", "주 2회"],
        ["글루트 브릿지", "12회 x 2세트", "주 2회"],
        ["카프 레이즈", "12회 x 2세트", "주 2회"],
        ["착지 자세 연습", "5회 x 2세트", "주 2회"]
    ],

    "높이뛰기": [
        ["글루트 브릿지", "12회 x 2세트", "주 2회"],
        ["한 발 균형 잡기", "20초 x 2세트", "주 2회"],
        ["제자리 무릎 들기", "10회 x 2세트", "주 2회"],
        ["도움닫기 리듬 연습", "5회 x 2세트", "주 2회"]
    ]
}


# ------------------------------------------
# 4. 점수 계산 함수
# ------------------------------------------

def calculate_score(gender, event, record):

    # 10m 왕복달리기
    if event == "10m 왕복달리기":

        standards = (
            run_male if gender == "남자"
            else run_female
        )

        record = round(record, 2)

        for i in range(24):

            if record <= standards[i]:
                raw_score = score_list[i]
                return raw_score, round(raw_score / 133 * 100, 1), None

        return 61, round(61 / 133 * 100, 1), None

    # 제자리 멀리뛰기
    elif event == "제자리 멀리뛰기":

        standards = (
            jump_male if gender == "남자"
            else jump_female
        )

        record = int(record)

        for i in range(24):

            if record >= standards[i]:
                raw_score = score_list[i]
                return raw_score, round(raw_score / 133 * 100, 1), None

        return 61, round(61 / 133 * 100, 1), None

    # 높이뛰기
    elif event == "높이뛰기":

        standards = (
            height_male if gender == "남자"
            else height_female
        )

        record = int(record)

        for i in range(len(standards)):

            if record >= standards[i]:
                return (
                    height_scores[i],
                    height_scores[i],
                    height_grades[i]
                )

        return 61, 61, "E"


# ------------------------------------------
# 5. 보강운동 판단 함수
# ------------------------------------------

def check_exercise(score):

    if score >= 90:
        return "현재 기록이 우수합니다. 유지 운동을 추천합니다."

    elif score >= 85:
        return "기록이 양호합니다. 부족한 부분을 보완하세요."

    elif score >= 70:
        return "기록 향상을 위해 보강운동을 추천합니다."

    else:
        return "기초 체력과 종목별 기술 보강을 추천합니다."


# ------------------------------------------
# 6. 운동 추천 표 출력 함수
# ------------------------------------------

def show_exercise(event):

    st.subheader("💪 맞춤형 보강운동")

    data = exercise_list[event]

    # 표에 들어갈 자료 만들기
    table_data = []

    for exercise in data:

        table_data.append({
            "운동 이름": exercise[0],
            "횟수 및 세트": exercise[1],
            "운동 주기": exercise[2]
        })

    st.table(table_data)


# ------------------------------------------
# 7. 결과 출력 함수
# ------------------------------------------

def show_result(gender, event, record):

    raw_score, score, grade = calculate_score(
        gender, event, record
    )

    st.divider()

    st.header("📊 실기 측정 결과")

    st.write(f"**성별:** {gender}")
    st.write(f"**실기 종목:** {event}")

    if event == "10m 왕복달리기":
        st.write(f"**측정 기록:** {record:.2f}초")

    elif event == "제자리 멀리뛰기":
        st.write(f"**측정 기록:** {record:.0f}cm")

    else:
        st.write(f"**측정 기록:** {record:.0f}cm")

    st.metric(
        label="100점 만점 환산 점수",
        value=f"{score}점"
    )

    if event == "높이뛰기":

        st.write(f"**고려대 실기 등급:** {grade}")
        st.write(f"**공식 기준표 배점:** {raw_score}점")

    else:

        st.write(f"**고려대 실기 기준표 배점:** {raw_score}점 / 133점")

    st.divider()

    # 운동 능력 분석
    st.subheader("🔍 운동 능력 분석")

    result = check_exercise(score)

    if score >= 90:
        st.success(result)

    elif score >= 70:
        st.info(result)

    else:
        st.warning(result)

    # 보강운동 추천
    if score < 90:

        show_exercise(event)

    else:

        st.write(
            "현재 기록을 유지하기 위한 가벼운 운동과 "
            "충분한 휴식을 추천합니다."
        )

    st.caption(
        "운동 횟수와 주기는 참고용이며, 개인의 체력과 "
        "회복 상태에 따라 조절하세요."
    )


# ------------------------------------------
# 8. 앱 메인 화면
# ------------------------------------------

st.header("1️⃣ 기본 정보 입력")

gender = st.selectbox(
    "성별을 선택하세요.",
    ["남자", "여자"]
)

st.header("2️⃣ 실기 종목 선택")

event = st.selectbox(
    "측정할 실기 종목을 선택하세요.",
    [
        "10m 왕복달리기",
        "제자리 멀리뛰기",
        "높이뛰기"
    ]
)


# ------------------------------------------
# 9. 종목별 기록 입력 화면
# ------------------------------------------

st.header("3️⃣ 실기 기록 입력")

if event == "10m 왕복달리기":

    st.caption("10m × 4 왕복달리기 기록을 입력하세요.")

    record = st.number_input(
        "기록 (초)",
        min_value=1.0,
        max_value=30.0,
        value=10.0,
        step=0.01
    )

elif event == "제자리 멀리뛰기":

    record = st.number_input(
        "기록 (cm)",
        min_value=1.0,
        max_value=500.0,
        value=200.0,
        step=1.0
    )

else:

    record = st.number_input(
        "기록 (cm)",
        min_value=1.0,
        max_value=250.0,
        value=120.0,
        step=1.0
    )


# ------------------------------------------
# 10. 결과 확인 버튼
# ------------------------------------------

st.divider()

if st.button("실기 점수 및 보강운동 확인하기", type="primary", use_container_width=True):

    show_result(gender, event, record)

st.divider()

st.caption(
    "본 프로그램은 고려대학교 2026학년도 공개 자료를 "
    "참고한 연습용 프로그램입니다. "
    "실제 입시 지원 전 최신 모집요강을 확인하세요."
)
