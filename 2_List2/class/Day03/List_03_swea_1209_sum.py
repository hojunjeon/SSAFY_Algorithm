import sys

sys.stdin = open('input.txt', 'r')

# T = int(input())
T = 10

for tc in range(1, T + 1):
    '''
    1. 행 우선 순회 -> 최댓값
    2. 열 우선 순회 -> 최댓값
    3. 대각선 순회 -> 최댓값
    4. 1 ~ 3 각 단계의 최댓값을 비교해 최대 최댓값을 print
    '''
    case_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 1. 행 우선 순회
    row_max = 0
    for y in range(100):
        temp = 0
        # for x in range(100):
        #     temp += arr[y][x]
        temp = sum(arr[y]) # -> y행의 x (0~99) 합
        if row_max < temp:
            row_max = temp

    # 2. 열 우선 순회
    col_max = 0
    for x in range(100):
        temp = 0
        # for y in range(100):
        #     temp += arr[y][x]
        temp = sum(row[x] for row in arr) # -> x열의 y (0 ~ 99) 합
        if col_max < temp:
            col_max = temp

    # 3. 대각선 순회
    cross_max = 0
    l2r = 0
    r2l = 0
    for y in range(100):
        for x in range(100):
            if y == x:
                l2r += arr[y][x]
            if y == 99 - x:
                r2l += arr[y][x]

    cross_max = max(l2r, r2l)

    max_sum = max(row_max, col_max, cross_max)

    print(f'#{tc} {max_sum}')
