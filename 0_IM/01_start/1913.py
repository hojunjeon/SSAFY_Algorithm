# 입문 1913 달팽이 숫자
from pprint import pprint

import sys
sys.stdin = open('SSAFY_Algorithm\\0_IM\\01_start\input.txt','r')

n = int(input())
goal = int(input())
snail = [[0] * n for _ in range(n)]

y = x = n // 2
dir = 0 # 위 - 오 - 아 - 왼
way = [[0, -1], [-1, 0], [0, 1], [1, 0]]

for i in range(1, n**2 + 1):
    '''
    1. snail[y][x] = i
    2. 방향을 돌린 곳이 0(빈 공간) 이면 방향을 돌리고(dir += 1) 숫자가 차 있으면 방향 유지
    3. y += way[dir % 4] / x += way[dir % 4]
    4. goal이 존재하는 지 확인하며 snail을 한 줄씩 print
        - goal 존재 시: goal_y = y / goal_x = snail[y].index(goal)
    '''
    snail[y][x] = i
    ny = y + way[(dir + 1) % 4][0]
    nx = x + way[(dir + 1) % 4][1]

    if snail[ny][nx] == 0:
        dir += 1
    y += way[dir % 4][0]
    x += way[dir % 4][1]
        
for y in range(n) :
    if goal in snail[y] :
        goal_x = snail[y].index(goal)
        goal_y = y
    print(*snail[y])

print(goal_y + 1, goal_x + 1)
