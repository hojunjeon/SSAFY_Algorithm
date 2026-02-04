#방향 배열 활용하기
import sys
sys.stdin = open("input.txt", "r")

# 상하좌우 순서의 델타 리스트
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

y, x = 3, 1

# 상하좌우 4방향
for i in range(4):
    now_y = y + dy[i]
    now_x = x + dx[i]
    print(now_y, now_x)

print()
# ------------------------------

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

y, x = 3, 1

# 대각선 포함 8방향 확인
for i in range(8):
    now_y = y + dy[i]
    now_x = x + dx[i]
    print(now_y, now_x)