import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    '''
    1. 행 우선 순회 
        - dx : 0 -> m-1 / dy : 0 -> m-1 : 델타를 x, y를 1씩 증가시켜가며 arr의 값을 더해나감 
    '''
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_kill = 0

    for y in range(n):
        for x in range(n):
            temp = 0
            for dx in range(m):
                for dy in range(m):
                    if (y + dy >= n) or (x + dx >= n):
                        continue
                    add = arr[y + dy][x + dx]
                    temp += add

            if max_kill < temp:
                max_kill = temp

    print(f'#{tc} {max_kill}')