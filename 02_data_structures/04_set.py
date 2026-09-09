"""
    집합 set
"""

# 중복 불가, 순서 x, 수정 o

nums = {1, 2, 3, 3, 3, 4, 2}
print(f"nums : {nums}")

# 비어 있는 상태 표현
empty1 = {}     # 딕셔너리를 나타냄!
empty2 = set()

print(f"empty1 : {type(empty1)}")
print(f"empty2 set() : {type(empty2)}")

nums = [1, 2, 3, 3, 3, 4, 2]
print(f"원본 데이터 : {nums}")
print(f"중복 제거 : {set(nums)}")
print(f"중복 제거 : {list(set(nums))}")
print()

# 집합 연산
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"합집합 | : {a | b}")
print(f"교집합 & : {a & b}")
print(f"차집합 - : {a - b}")
print(f"차집합 - : {b - a}")

# 데이터 변경
data = {1, 2}
print(f"data : {data}")

# 추가 : add (1개의 값을 추가 시 add 사용)
data.add(3)
print(f"data : {data}")

# update (여러 개의 값을 추가 시 update 사용)
data.update([4, 5])
print(f"data : {data}")

data.update([4, 5, 6, 7])
print(f"data : {data}")

# 삭제  discard
data.discard(1)
print(f"data : {data}")

data.discard(99)
print(f"data : {data}")