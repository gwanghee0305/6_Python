"""
    문자열 다루기
"""

print("=" * 60)
print("인덱싱, 슬라이싱")
print("=" * 60) 

# 인덱스는 0부터 시작

message = "No pain, No gain"
print(f"메세지 : {message}")
print()
# 인덱싱 : 변수명[인덱스] => 특정 위치의 문자 추출
print(f"첫글자 : {message[0]}")
print(f"마지막글자 : {message[-1]}")

# 슬라이싱 : 변수 [시작인덱스 : 끝인덱스 : step]
print(f"{message[0:7:1]} / {message[0:7]} / {message[:7]}")  # 0~6까지 추출
print(f"{message[7:]}")  # 7~끝까지 추출
print(f"{message[::2]}")  # 0~끝까지 2칸씩 건너뛰며 추출
print(f"{message[::-1]}")  # 0~끝까지 역순으로 추출

print("=" * 60)
print("다양한 문자열 메소드")
print("=" * 60)

# 대문자 변환 : upper()
print(f"대문자 변환 : {message.upper()}")
# 소문자 변환 : lower()
print(f"소문자 변환 : {message.lower()}")

message = "   Hello, Python World   "
print(f"[{message}]")
# 좌우 공백 제거 : strip()
print(f"좌우 공백 제거 : [{message.strip()}]")

# 문자열을 구분자로 분할 : split(구분자)
print(f"split : [{message.split(',')}]")

# 특정 문자 개수 반환 : count(문자)
print(f"l의 개수: {message.count('l')}")

# 특정 문자의 인덱스 반환 : find(문자) => 없으면 -1 반환
print(f"Python의 위치 : {message.find('Python')}")
print(f"Java의 위치 : {message.find('Java')}")

# 리스트 --> 문자열(문자열 결합)
today = '-'.join(['2026', '09', '07'])
print(f"today : {today} ({type(today)})")

print("=" * 60)

# 여러 줄 문자열 => 따옴표 3개 사용
end_message = """
    문자열 다루기
    - 인덱싱, 슬라이싱
    - 자주 사용하는 메소드 (split, join, strip, ...)
"""

print(end_message)