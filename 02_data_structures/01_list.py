"""
    리스트(list)
"""

# 리스트 데이터 표현 : 대괄호 사용 [] 
colors = ["red", "green", "blue"]

print(f"colors -> {colors}")
# 첫 번째 요소 출력
print(f"첫 번째 : {colors[0]}")
# 마지막 요소 출력
print(f"마지막 : {colors[2]}")
print(f"마지막 : {colors[-1]}")

print(f"{colors[0:2]}")

# 다양한 타입의 데이터를 담을 수 있음
mixed = [100, "Hello", True, [1,2,3]]
print(f"mixed : {mixed}")

# 리스트 상태에 따라 bool 타입 확인
temp = []
print(f"mixed --> {bool(mixed)}")
print(f"temp --> {bool(temp)}")

print("=" * 60)
items = ["페페로니", "고구마", "포테이토"]

print(f"items --> {items}")

# 데이터 추가 : append(), insert(), extend()
items.append("불고기")
print(f"append - 맨 뒤에 추가 : {items}")

items.insert(2, "콤비")
print(f"insert - 위치를 지정해서 추가: {items}")

items.extend(["꼬북칭","허니버터"])
print(f"extend")

# 수정 / ㅅ삭제
print("=" * 60)
items[0] = "ACE"
print(f"특정 인덱스를 지엉하여 값을 견경 :{items}")

items.remove("고구마")
print(f"특정 인덱스를 지엉하여 값을 견경 :{items}")

snack = items.pop()
print(f"pop - {snack} / {items}")    # 맨뒤에 데이터를 삭제 후 반환

del items[0]
print(f"del - 인덱스로 삭제: {items}")

# 탐색, 정보 조회
numbers = [5, 1, 2, 7, 9, 4, 1]

# 찾을 값 in 리스트 => 값이 있으면 True, 없으면 False
# 리스트.index(찾을값) => 값이 있으면 해당 인덱스, 없으면 오류 발생

print(f"numbers 에 7이 있는지? {7 in numbers}")
print(f"numbers 에 7이 있는지? {numbers.index(7)}")

print(f"numbers 에 3이 있는지? {3 in numbers}")
# print(f"numbers에 3이 있는지 ? {numbers.index(3)}")

print(f"numbers 에서 1의 개수 : {numbers.count(1)}")
print(f"numbers 에서 3의 개수 : {numbers.count(3)}")

print(f"리스트 길이 : {len(numbers)}")
numbers.sort()      # 해당 리스트의 값을 변경
print(f"sort -> {numbers}")
numbers.sort(reverse=True)
print(f"sort(reverse=True) -> {numbers}")

fruits = ["banana", "cherry", "apple"]
fruits.sort()
print(f"문자열 정렬 -> {fruits}")
fruits.reverse()    # 해당 리스트를 역순으로 변경
print(f"reverse() -> {fruits}")

print("=" * 60)

# 2차원 리스트
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"(1,1) -> {matrix[1][1]}")
print()

for row in matrix:
    # print(row)
    for value in row:
        print(value, end=" ")
    print()