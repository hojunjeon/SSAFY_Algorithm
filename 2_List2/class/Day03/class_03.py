# 비트 연산
# - bit : 0 or 1 을 나타내는 값
# - bit 의 개념을 활용하는 연산

print(1)
print(1 << 1)  # 0010(2) = 2
print(1 << 2)  # 0100(2) = 4

# -------------------

# 전체 부분집합 구하는 과정

arr = [1, 2, 3]
n = len(arr)

subsets = []

# 1 << n : 전체 부분집합의 수
for mask in range(1 << n):        # 0 ~ 2^n - 1
    subset = []
    # i : 각 자리수
    for i in range(n):
        # if mask & (1 << i) : 해당 자리 수의 숫자가 현재 부분집합에 포함 되어 있는 지?
        if mask & (1 << i):       # i번째 비트가 1인지 확인
            subset.append(arr[i])
    subsets.append(subset)

print(subsets)

# ---------------------------

# =========================
# 상태 비트 정의
# =========================
ATTACK = 1 << 0   # 0001
JUMP   = 1 << 1   # 0010
MOVE   = 1 << 2   # 0100
DEFEND = 1 << 3   # 1000


def print_status(status):
    states = []
    if status & ATTACK: states.append("ATTACK")
    if status & JUMP:   states.append("JUMP")
    if status & MOVE:   states.append("MOVE")
    if status & DEFEND: states.append("DEFEND")

    if not states:
        print("대기 상태")
    else:
        print(" + ".join(states))


# =========================
# 예제 1 : 대기 상태
# =========================
STATUS = 0
print("예제 1")
print_status(STATUS)
print()


# =========================
# 예제 2 : 공격 중
# =========================
STATUS = ATTACK
print("예제 2")
print_status(STATUS)
print()


# =========================
# 예제 3 : 이동하면서 공격
# =========================
STATUS = MOVE | ATTACK
print("예제 3")
print_status(STATUS)
print()


# =========================
# 예제 4 : 점프 공격
# =========================
STATUS = JUMP | ATTACK
print("예제 4")
print_status(STATUS)
print()


# =========================
# 예제 5 : 방어하면서 이동
# =========================
STATUS = DEFEND | MOVE
print("예제 5")
print_status(STATUS)
print()
