# import sys
#
# sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    '''
    1. 행 우선 순회하며 델타를 리스트로 하여 중앙값+상하좌우 1칸의 값을 합
        - 좌표값이 0 ~ n-1 사이일 때만 동작
    2. 부분합이 전체 최댓값일 경우 max_kill = temp / coordinate [y,x] 를 삽입
    '''
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_kill = 0
    coordinate = [0, 0]
    del_list = [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]

    for y in range(n):
        for x in range(n):
            temp = 0
            for di, dj in del_list:
                if (0 <= y + di < n) and (0 <= x + dj < n):
                    temp += arr[y + di][x + dj]

            if max_kill < temp:
                max_kill = temp
                coordinate = [y, x]

    print(f'#{tc} {max_kill} {coordinate[0]} {coordinate[1]}')