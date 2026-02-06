import sys
sys.stdin = open("input.txt", "r")


# 1. 현재 숫자(current) 가 1부터 N^2 까지 반복
# 2. 방향배열 : 우하좌상 순서
# 3. 바라보고 있는 방향 -> 계속 전진
#   - 방향 회전
#     - 벽을 만나거나
#     - 이미 숫자가 있는 곳을 만나면

# 방향배열 (우하좌상)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    y, x = 0, 0
    current = 1
    direction = 0  # 현재 바라보고 있는 방향

    while current <= N * N:
        arr[y][x] = current  # 현재 자리에 숫자 저장

        # 다음 좌표를 갈 수 있는 곳인지 체크하는 코드 ------
        ny = y + dy[direction]
        nx = x + dx[direction]

        # if 다음좌표가 범위 밖 or 이미 데이터가 있다면:
        #     방향전환
        if ny < 0 or ny >= N or nx < 0 or nx >= N or arr[ny][nx]:
            # 0 1 2 3 0 1 2 3 을 반복해야함
            direction = (direction + 1) % 4

        # --------------------------------------

        current += 1  # 다음 숫자
        # 방향이 바뀌지 않았다면, 해당 방향으로 전진
        # 방향이 바뀌었다면, 바뀐 방향으로 전진
        y = y + dy[direction]  # 다음 좌표로 이동
        x = x + dx[direction]  # 다음 좌표로 이동

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])