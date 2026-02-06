import sys
sys.stdin = open('input.txt', 'r')

# T = int(input())

for _ in range(1, 11):
    '''
    1. 사다리의 도착지점 찾기 end
    2. 사다리 맨 아랫지점[99, end] 에서 역주행 하며 경로를 찾음
        # 이전 상태 기록 ACTION = UP / LEFT / RIGHT
        - 1. 사다리 왼쪽에 1이 있다면 : x -= 1
        - 2. 오른쪽에 1이 있다면 : x+= 1
        - 3. 둘다 아니라면 y -= 1
    3. 모두 순회한 이후 최종 x값 반환
    '''
    tc = int(input())
    ladder = [list(input().split()) for _ in range(100)]

    end = ladder[-1].index('2')

    x = end
    y = 99
    ACTION = 'UP'

    while y > 0:

        if ACTION == 'UP':
            if x != 99 and ladder[y][x + 1] == '1':
                x += 1
                ACTION = 'RIGHT'
            elif x != 0 and ladder[y][x - 1] == '1':
                x -= 1
                ACTION = 'LEFT'
            else:
                y -= 1

        elif ACTION == 'LEFT':
            if ladder[y - 1][x] == '1':
                y -= 1
                ACTION = 'UP'
            else:
                x -= 1

        elif ACTION == 'RIGHT':
            if ladder[y - 1][x] == '1':
                y -= 1
                ACTION = 'UP'
            else:
                x += 1

    print(f'#{tc} {x}')
