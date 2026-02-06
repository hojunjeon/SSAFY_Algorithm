import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    '''
    # 바라보는 방향(pos)을 숫자로 표현 (Right : 0 / Down : 1 / Left : 2 / Up : 3 )
    # pos에 따라 적용되는 값 달라짐 ( 0:x+1 / 1:y+1 / 2:x-1 / 3:y-1 )
    1. i : 1 -> n^2
        - 1. arr[y][x] 에 i 삽입
        - 2. 좌표 체크
            - 1 ) pos에 따라 전진 시 인덱스 범위를 벗어나면
                    pos += 1 (시계방향 90도 회전)
            - 2 ) pos에 따라 전진 
    '''
    n = int(input())

    y, x = 0, 0
    arr = [[0 for _ in range(n)] for _ in range(n)]

    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 우 하 좌 상
    pos = 0
    N = (n ** 2) + 1

    for i in range(1, N):
        arr[y][x] = i

        ny = y + direction[pos][0]
        nx = x + direction[pos][1]

        if ny < 0 or ny >= n or nx < 0 or nx >= n or arr[ny][nx] != 0:
            pos = (pos + 1) % 4
            ny = y + direction[pos][0]
            nx = x + direction[pos][1]

        y, x = ny, nx

    print(f'#{tc}')
    for i in range(n):
        print(*arr[i])