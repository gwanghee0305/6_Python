"""
1. 몸무게(kg)와 키(cm)를 입력받아 BMI 지수를 계산하는 함수를 정의

- BMI = 몸무게(kg) / (키(m) * 키(m))
- 키는 cm로 입력받아 m로 변환
- 반올림 함수: `round(숫자, 자릿수)`

몸무게를 입력하세요(kg): 70
키를 입력하세요(cm): 175

BMI: 22.86
"""
# weight = input("몸무게를 입력하세요(kg): ")
# height = input("키를 입력하세요(cm): ")

# weight = float(weight)
# height = float(height)
# height = float(height / 100)

# bmi = weight / (height * height)

# print(f"BMI: {round(bmi, 2)}")

"""
2. 여러 개의 숫자를 입력받아 평균을 계산하는 함수를 정의

- 사용자가 'q'를 입력할 때까지 숫자를 계속 입력받음 (입력받는 개수는 정해져 있지 않음)
- 평균 = 총합 / 총개수

========== 평균 계산기 ==========
숫자 입력 (q 입력 시 종료) : 1
숫자 입력 (q 입력 시 종료) : 4
숫자 입력 (q 입력 시 종료) : 5
숫자 입력 (q 입력 시 종료) : q

---> 평균: 3.33

========== 평균 계산기 ==========
숫자 입력 (q 입력 시 종료) : 1
숫자 입력 (q 입력 시 종료) : q

---> 평균: 1.0

========== 평균 계산기 ==========
숫자 입력 (q 입력 시 종료) : q

---> 값이 없습니다.
"""
# numbers = []

# print("========== 평균 계산기 ==========")

# while True:
#     value = input("숫자 입력 (q 입력 시 종료) : ")
#     if value == "q":
#         break
#     numbers.append(float(value))
# if len(numbers) == 0:
#     print("\n---> 값이 없습니다.")
# else:
#     average = sum(numbers) / len(numbers)

#     print(f"\n---> 평균: {round(average, 2)}")

"""
3. 단어 빈도수 분석 함수 정의

- 문장(문자열)을 입력받아 공백 단위로 단어를 분리하고, 각 단어의 등장 횟수를 딕셔너리로 계산하여 반환
- 대소문자를 구분하지 않도록 모든 문자를 소문자로 변환하여 처리
- 소문자 변환: .lower()
- 문자열 분리: .split()

문장을 입력하세요: Python is fun and Python is powerful

[단어 빈도수 결과]
- python: 2회
- is: 2회
- fun: 1회
- and: 1회
- powerful: 1회
"""
text = input("문장을 입력하세요: ")

print("[단어 빈도수 결과]")
text2 = text.lower()
text2.split(" ")

space = {}
for w in text2:
