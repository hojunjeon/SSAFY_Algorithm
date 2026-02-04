import sys
sys.stdin = open("input.txt", "r")

# 상하좌우 델타
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_y, max_x, max_total = 0, 0, 0

    # sy, sx : 파리채를 치는 지점
    for sy in range(N):
        for sx in range(N):
            # (sy, sx) + 상하좌우 값 -> 더한다.
            total = arr[sy][sx]

            for i in range(4):
                new_y = sy + dy[i]
                new_x = sx + dx[i]

                # 해당 방향의 좌표가 범위를 벗어나면 continue
                if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N:
                    continue

                total += arr[new_y][new_x]

            # 최대값 갱신
            if total > max_total:
                max_y = sy
                max_x = sx
                max_total = total

    print(f"#{tc} {max_total} {max_y} {max_x}")