"""
    형변환
"""

print("=" * 60)
print("문자열 --> 숫자")
print("=" * 60)

print(f"'100' --> {int('100')}")
print(f"'3.14' --> {float('3.14')}")

#print(f"'3.14' --> {int('3.14')}")  # ValueError: invalid literal for int() with base 10: '3.14'
print(f"'3.14' --> {int(float('3.14'))}")  # 실수 형태의 문자열은 바로 int 변환 불가
# float로 변환 후 정수로 변환

print("=" * 60)
print("숫자 --> 문자열")
print("=" * 60)

print (str(1000) + "원)")

print("=" * 60)
print("bool 타입 변환")
print("=" * 60)

falsy_values = [0, 0.0, "",  [], (), {}, set(), None, False]
truthy_values = [1, -1, 0.1, "0", "False", [0], " "]

print("== falsy (거짓으로 취급되는 값) ==")
for v in falsy_values:
    print(f"{str(v) :<10} -> {bool(v)}")

print("== truthy (참으로 취급되는 값) ==")
for v in truthy_values:
    print(f"{str(v) :<10} -> {bool(v)}")







