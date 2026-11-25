# 연세대학교 체대입시 실기 기준표 반영 가이드 및 보강운동 프로그램

# 1. 연세대 기준 성별/종목별 배점 테이블 (리스트 활용)
# 형식: [[기록기준, 배점], ...] -> 위에서부터 순서대로 조건 검사
YONSEI_TABLE = {
    "남자": {
        "10m": [  # 10m 왕복달리기 (초 이하 기준)
            [9.30, 100], [9.45, 96], [9.60, 92], [9.75, 88],
            [9.90, 84],  [10.05, 80], [10.20, 76], [10.40, 72]
        ],
        "제자리 멀리뛰기": [  # 제자리 멀리뛰기 (cm 이상 기준)
            [285, 100], [280, 96], [275, 92], [270, 88],
            [265, 84],  [260, 80], [255, 76], [250, 72]
        ],
        "메디신볼": [  # 메디신볼 던지기 3kg (m 이상 기준)
            [13.5, 100], [13.0, 96], [12.5, 92], [12.0, 88],
            [11.5, 84],  [11.0, 80], [10.5, 76], [10.0, 72]
        ]
    },
    "여자": {
        "10m": [  # 10m 왕복달리기 (초 이하 기준)
            [10.30, 100], [10.45, 96], [10.60, 92], [10.75, 88],
            [10.90, 84],  [11.05, 80], [11.20, 76], [11.40, 72]
        ],
        "제자리 멀리뛰기": [  # 제자리 멀리뛰기 (cm 이상 기준)
            [235, 100], [230, 96], [225, 92], [220, 88],
            [215, 84],  [210, 80], [205, 76], [200, 72]
        ],
        "메디신볼": [  # 메디신볼 던지기 2kg (m 이상 기준)
            [10.0, 100], [9.6, 96], [9.2, 92], [8.8, 88],
            [8.4, 84],   [8.0, 80], [7.6, 76], [7.2, 72]
        ]
    }
}

# 2. 종목별 보강운동 추천 리스트 [보강운동명, 횟수/세트, 주기]
WORKOUTS = {
    "10m": [
        ["사다리 스텝 훈련 (민첩성)", "5세트", "주 3회"],
        ["터치 턴 왕복 스프린트", "10회 x 3세트", "주 3회"],
        ["플랭크 & 러시안 트위스트", "1분 x 3세트", "주 4회"]
    ],
    "제자리 멀리뛰기": [
        ["박스 점프 (순발력)", "10회 x 4세트", "주 3회"],
        ["바벨 스쿼트 (하체 근력)", "8회 x 4세트", "주 2회"],
        ["서전트 점프 & 암 스윙", "15회 x 3세트", "주 3회"]
    ],
    "메디신볼": [
        ["오버헤드 메디신볼 슬램", "12회 x 4세트", "주 3회"],
        ["푸시업 & 딥스 (상체 근력)", "15회 x 4세트", "주 3회"],
        ["행잉 레그레이즈 (코어)", "15회 x 3세트", "주 4회"]
    ]
}


# 3. 연세대 기준표 기반 점수 계산 함수
def calculate_yonsei_score(gender, event, record):
    table = YONSEI_TABLE[gender][event]
    default_min_score = 68  # 표의 최하위 구간 미만일 때 기본 점수

    # 반복문과 조건문으로 구간별 배점 확인
    for standard, score in table:
        if event == "10m":  # 기록이 낮을수록 높은 점수
            if record <= standard:
                return score
        else:  # 기록이 높을수록 높은 점수
            if record >= standard:
                return score

    return default_min_score


# 4. 결과 및 보강운동 표 출력 함수
def print_report(gender, event, record, score):
    unit = "초" if event == "10m" else ("cm" if event == "제자리 멀리뛰기" else "m")
    
    print("\n" + "=" * 58)
    print(" [ 연세대학교 체대입시 실기 분석 결과 리포트 ]")
    print("=" * 58)
    print(f" - 성별 / 종목 : {gender} / {event}")
    print(f" - 입력 기록   : {record}{unit}")
    print(f" - 환산 점수   : {score}점 / 100점 만점 (연세대 기준)")
    print("-" * 58)

    # 연세대 합격권 기준(92점 이상 안정권, 92점 미만 보강 필요) 조건 분기
    if score == 100:
        print(" 판정: [만점] 연세대 실기 만점 기록입니다! 부상 방지에 집중하세요.")
    elif score >= 92:
        print(" 판정: [합격 안정권] 우수한 기록입니다. 감점 요인만 줄이세요.")
    else:
        print(" 판정: [보강 필요] 연세대 합격권(92점 이상) 진입을 위해 보강운동이 필요합니다.\n")
        
        # 표 헤더 출력
        print(f"{'보강운동':<26} | {'횟수':<14} | {'주기':<8}")
        print("-" * 58)
        
        # 반복문을 통해 보강운동 리스트를 표 형태로 출력
        for workout in WORKOUTS[event]:
            name, reps, cycle = workout
            print(f"{name:<24} | {reps:<13} | {cycle:<8}")

    print("=" * 58 + "\n")


# 5. 메인 실행 함수
def main():
    genders = ["남자", "여자"]
    events = ["10m", "제자리 멀리뛰기", "메디신볼"]

    print("=== 연세대학교 체대입시 실기 가이드 및 보강운동 프로그램 ===")

    # 성별 선택 (반복문으로 유효성 검사)
    while True:
        gender = input("\n성별을 입력하세요 (남자 / 여자): ").strip()
        if gender in genders:
            break
        print("잘못된 입력입니다. '남자' 또는 '여자'로 입력해주세요.")

    # 실기 종목 선택
    while True:
        print("\n[실기 종목 선택]")
        for i, ev in enumerate(events, 1):
            print(f"{i}. {ev}")
        
        choice = input("종목 번호 또는 이름을 입력하세요: ").strip()
        if choice in ["1", "10m"]:
            event = "10m"
            break
        elif choice in ["2", "제자리 멀리뛰기"]:
            event = "제자리 멀리뛰기"
            break
        elif choice in ["3", "메디신볼"]:
            event = "메디신볼"
            break
        else:
            print("잘못된 입력입니다. 1~3번 또는 정확한 종목명을 입력해주세요.")

    # 기록 입력
    unit_guide = "초 (예: 9.50)" if event == "10m" else ("cm (예: 278)" if event == "제자리 멀리뛰기" else "m (예: 12.8)")
    while True:
        try:
            record = float(input(f"\n'{event}' 기록을 입력하세요 [{unit_guide}]: "))
            if record > 0:
                break
            print("0보다 큰 숫자를 입력해주세요.")
        except ValueError:
            print("숫자만 정확히 입력해주세요.")

    # 점수 계산 및 결과 출력
    score = calculate_yonsei_score(gender, event, record)
    print_report(gender, event, record, score)


if __name__ == "__main__":
    main()
