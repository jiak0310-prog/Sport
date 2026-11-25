
# ==========================================
# 체대입시생을 위한 실기가이드 & 보강운동 추천
# 고려대학교 공개 실기 기준 참고 프로그램
# ==========================================


# 1. 실기 점수 기준표 (리스트)

# 10m 왕복달리기 점수표
# 2025학년도 공개 기록표 참고
score_list = [
    133, 130, 127, 124, 121,
    118, 115, 112, 109, 106,
    103, 100, 97, 94, 91,
    88, 85, 82, 79, 76,
    73, 70, 67, 64, 61
]

# 남자와 여자 기록 기준 (초)
run_male = [round(8.50 + 0.10*i, 2) for i in range(24)]
run_female = [round(9.50 + 0.10*i, 2) for i in range(24)]

# 제자리 멀리뛰기 기준 (cm)
jump_male = [300 - 3*i for i in range(24)]
jump_female = [250 - 3*i for i in range(24)]

# 높이뛰기 기준 (cm)
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
    93, 92, 85, 78, 71, 61
]


# 2. 종목별 보강운동 리스트

exercise_list = {
    "10m 왕복달리기": [
        ["사이드 스텝", "10회 x 2세트", "주 2회"],
        ["스쿼트", "10회 x 2세트", "주 2~3회"],
        ["방향 전환 연습", "5회 x 2세트", "주 2회"],
        ["짧은 가속 달리기", "10m x 3회", "주 2회"]
    ],

    "제자리 멀리뛰기": [
        ["스쿼트", "10회 x 2세트", "주 2~3회"],
        ["글루트 브릿지", "12회 x 2세트", "주 2~3회"],
        ["카프 레이즈", "12회 x 2세트", "주 2회"],
        ["멀리뛰기 착지 연습", "5회 x 2세트", "주 2회"]
    ],

    "높이뛰기": [
        ["제자리 무릎 들기", "10회 x 2세트", "주 2회"],
        ["글루트 브릿지", "12회 x 2세트", "주 2~3회"],
        ["한 발 균형 잡기", "20초 x 2세트", "주 2회"],
        ["도움닫기 리듬 연습", "5회 x 2세트", "주 2회"]
    ]
}


# 3. 성별 선택 함수

def select_gender():

    while True:
        print("\n===== 성별 선택 =====")
        print("1. 남자")
        print("2. 여자")

        choice = input("번호를 선택하세요: ")

        if choice == "1":
            return "남자"

        elif choice == "2":
            return "여자"

        else:
            print("잘못된 입력입니다. 다시 선택하세요.")


# 4. 실기 종목 선택 함수

def select_event():

    events = [
        "10m 왕복달리기",
        "제자리 멀리뛰기",
        "높이뛰기"
    ]

    while True:
        print("\n===== 실기 종목 선택 =====")

        for i in range(len(events)):
            print(f"{i+1}. {events[i]}")

        choice = input("종목 번호를 선택하세요: ")

        if choice in ["1", "2", "3"]:
            return events[int(choice)-1]

        else:
            print("1~3번 중에서 선택하세요.")


# 5. 실기 기록 입력 함수

def input_record(event):

    while True:
        try:
            print("\n===== 실기 기록 입력 =====")

            if event == "10m 왕복달리기":
                record = float(
                    input("10m 왕복달리기 기록(초): ")
                )

            elif event == "제자리 멀리뛰기":
                record = float(
                    input("제자리 멀리뛰기 기록(cm): ")
                )

            else:
                record = float(
                    input("높이뛰기 기록(cm): ")
                )

            if record <= 0:
                print("0보다 큰 기록을 입력하세요.")
                continue

            return record

        except ValueError:
            print("숫자로 입력해주세요.")


# 6. 점수 계산 함수

def calculate_score(gender, event, record):

    # 10m 왕복달리기
    if event == "10m 왕복달리기":

        standards = run_male if gender == "남자" else run_female

        for i in range(len(standards)):

            if record <= standards[i]:
                return round(score_list[i] / 133 * 100, 1)

        return round(61 / 133 * 100, 1)

    # 제자리 멀리뛰기
    elif event == "제자리 멀리뛰기":

        standards = jump_male if gender == "남자" else jump_female

        for i in range(len(standards)):

            if record >= standards[i]:
                return round(score_list[i] / 133 * 100, 1)

        return round(61 / 133 * 100, 1)

    # 높이뛰기
    elif event == "높이뛰기":

        standards = height_male if gender == "남자" else height_female

        for i in range(len(standards)):

            if record >= standards[i]:
                return height_scores[i]

        return 61


# 7. 보강운동 필요 여부 판단 함수

def check_exercise(score):

    if score >= 90:
        return "현재 기록이 우수합니다. 꾸준한 유지 운동을 추천합니다."

    elif score >= 85:
        return "기록이 양호합니다. 부족한 부분을 보완하세요."

    elif score >= 70:
        return "기록 향상을 위해 보강운동이 필요합니다."

    else:
        return "기초 체력 및 종목별 기술 보강이 필요합니다."


# 8. 결과 출력 함수

def show_result(gender, event, record, score):

    print("\n")
    print("=" * 55)
    print("          체대입시 실기 측정 결과")
    print("=" * 55)

    print(f"성별 : {gender}")
    print(f"실기 종목 : {event}")
    print(f"측정 기록 : {record}")

    print("-" * 55)

    print(f"환산 점수 : {score}점 / 100점")

    print("-" * 55)

    print("===== 운동 능력 분석 =====")

    result = check_exercise(score)

    print(result)

    # 점수에 따라 보강운동 추천
    if score < 85:

        print("\n===== 맞춤형 보강운동 추천 =====")

        print("-" * 55)

        print("{:<22}{:<18}{:<12}".format(
            "운동 이름", "횟수 및 세트", "주기"
        ))

        print("-" * 55)

        # 리스트를 반복문으로 출력
        for exercise in exercise_list[event]:

            print("{:<22}{:<18}{:<12}".format(
                exercise[0],
                exercise[1],
                exercise[2]
            ))

    else:

        print("\n현재 기록을 유지할 수 있도록")
        print("가벼운 유지 운동과 충분한 휴식을 추천합니다.")

    print("=" * 55)


# 9. 메인 실행 함수

def main():

    print("=" * 55)
    print("   체대입시생을 위한 실기가이드 & 보강운동 프로그램")
    print("                고려대학교 기준 참고")
    print("=" * 55)

    while True:

        # 성별 선택
        gender = select_gender()

        # 종목 선택
        event = select_event()

        # 기록 입력
        record = input_record(event)

        # 점수 계산
        score = calculate_score(
            gender, event, record
        )

        # 결과 출력
        show_result(
            gender, event, record, score
        )

        # 재실행 여부
        again = input(
            "\n다른 종목도 측정하시겠습니까? (y/n): "
        )

        if again.lower() != "y":

            print("\n프로그램을 종료합니다.")
            break


# 프로그램 실행
main()
