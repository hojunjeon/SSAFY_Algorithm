#이차원 리스트 다뤄보기
import sys
sys.stdin = open("input.txt", "r")

# 1. 입력
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 2. 가로부터 접근
for y in range(5):
    for x in range(5):
        # print(y, x)  # 좌표값 출력
        print(arr[y][x], end=' ')

    print()

print('---------------------------------')

# 3. 세로부터 접근
# for x in range(5):
#     for y in range(5):
#         print(arr[y][x], end=' ')
#
#     print()

# 반복문은 고정하고, 내부 위치만 바꿔도 된다.
for i in range(5):
    for j in range(5):
        print(arr[j][i], end=' ')
    print()

print('---------------------------------')

# 4. 대각선 접근
# 4.1 우하단 대각선 (\)
for i in range(5):
    print(arr[i][i])

print('---------------------------------')

# 4.2 좌하단 대각선 (/)
for i in range(5):
    # print(i, 4-i)
    print(arr[i][4-i])

print('---------------------------------')

# 5. 범위 접근
# - 3*3 사각형 범위값들을 한 번에 접근
# - 예시) 합이 가장 큰 3*3 범위 값을 구하여라


# 출발지를 전달받아서, 3*3 영역의 합을 계산하는 함수
def cal_total(sy, sx):
    total = 0
    for y in range(sy, sy + 3):  # 출발지 ~ 출발지 + 3
        for x in range(sx, sx + 3):
            # 범위 밖 계산 체크를 항상 합시다!
            # 1. [권장] 범위 밖은 계산하지 마라
            if y > 4 or y < 0 or x > 4 or x < 0:
                continue

            total += arr[y][x]

            # 2. 범위 안에 들어왔을 때만 계산해라
            #   - 추후 조건이 많아지면 가독성이 떨어진다.
            # if 0 <= y <= 4 and 0 <= x <= 4:
            #     total += arr[y][x]

    return total


max_total = 0
max_y, max_x = 0, 0

# 계산하고자 하는 출발지를 반복
for sy in range(5):
    for sx in range(5):
        total = cal_total(sy, sx)
        # max_total = max(max_total, total)  # 값만 필요하다면
        # 좌표값까지 같이 저장
        if total > max_total:
            max_total = total
            max_y = sy
            max_x = sx

print(max_y, max_x, max_total)