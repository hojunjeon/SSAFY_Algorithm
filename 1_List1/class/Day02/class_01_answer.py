arr = [5, 1, 4, 2, 3]

# [문제 1]
# 정수 리스트를 오름차순으로 정렬하세요.
# - list.sort() 를 사용할 것
# - 원본 리스트가 변경되는지 확인하세요
# - 반환값이 있는지 확인하세요
arr.sort()  # 원본 리스트 자체가 변경됨, 반환값은 None

print("기본 리스트:", arr)


words = ["apple", "banana", "kiwi"]

# [문제 2]
# 문자열 리스트를 "문자열 길이" 기준으로 오름차순 정렬하세요.
# - key 옵션을 반드시 사용하세요
# - lambda 식을 사용하세요
# - 각 원소의 길이를 어떻게 꺼낼지 고민해보세요
words.sort(key=lambda x: len(x))

print("문자열 리스트:", words)


data = [(1, 90), (3, 80), (2, 90)]

# [문제 3-1]
# 튜플 리스트를 기본 정렬 기준으로 정렬하세요.
# - key 옵션 없이 정렬했을 때 어떤 값이 기준이 되는지 확인하세요
data.sort()

# [문제 3-2]
# 튜플의 두 번째 값(점수)을 기준으로 오름차순 정렬하세요.
# - lambda 를 사용하세요
# - x[1] 이 의미하는 바를 생각해보세요
data.sort(key=lambda x: x[1])

# [문제 3-3]
# 점수 오름차순, 점수가 같으면 첫 번째 값 오름차순으로 정렬하세요.
# - key 에서 튜플을 반환하도록 작성하세요
data.sort(key=lambda x: (x[1], x[0]))

# [문제 3-4]
# 점수는 내림차순, 첫 번째 값은 오름차순으로 정렬하세요.
# - 숫자 내림차순을 어떻게 표현하는지 고민해보세요
data.sort(key=lambda x: (-x[1], x[0]))

print("튜플 리스트:", data)


scores = {
    "kim": 90,
    "lee": 85,
    "park": 90
}

# [문제 4-1]
# 딕셔너리를 key 기준으로 정렬하세요.
# - dict 자체는 정렬되지 않음을 기억하세요
# - items() 를 사용해야 하는 이유를 생각해보세요
sorted_by_key = sorted(scores.items())

# [문제 4-2]
# 딕셔너리를 value 기준으로 오름차순 정렬하세요.
# - lambda 에서 x[0], x[1] 이 각각 무엇인지 확인하세요
sorted_by_value = sorted(scores.items(), key=lambda x: x[1])

# [문제 4-3]
# value 기준 내림차순으로 정렬하세요.
# - reverse 옵션을 사용할지, key 에서 처리할지 고민해보세요
sorted_by_value_desc = sorted(scores.items(), key=lambda x: x[1], reverse=True)

print("딕셔너리 key 기준 정렬:", sorted_by_key)
print("딕셔너리 value 기준 정렬:", sorted_by_value)
print("딕셔너리 value 내림차순 정렬:", sorted_by_value_desc)
print("딕셔너리:", scores)


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name}:{self.score}"


students = [
    Student("kim", 90),
    Student("lee", 85),
    Student("park", 90)
]

# [문제 5-1]
# Student 객체 리스트를 점수 기준 오름차순으로 정렬하세요.
# - 객체 자체는 비교가 불가능함을 떠올리세요
# - key 에서 어떤 값을 반환해야 할지 생각해보세요
students.sort(key=lambda s: s.score)

# [문제 5-2]
# 점수는 내림차순, 이름은 오름차순으로 정렬하세요.
# - 다중 기준 정렬입니다
# - 튜플을 반환하는 key 를 작성하세요
students.sort(key=lambda s: (-s.score, s.name))

print("학생 객체 리스트:", students)