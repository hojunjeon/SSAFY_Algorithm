import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    '''
    # 흰색 : 1 / 검정색 : 0
    1. 행 순회
        - 1. arr[y][x-1], arr[y][x+k] == 0 이고 arr[y][x] ~ arr[y][x+k-1] == 1 이면
            count += 1
    2. 열 순회
        - 1. arr[y-1][x], arr[y+k][x] == 0 이고 arr[y][x] ~ arr[y+k-1][x] == 1 이면
            count += 1
    '''

    def k_length_word(arr):
        cnt = 0
        # 행 우선 순회
        for y in range(n):
            for x in range(n - k + 1):

                # x -> x + k - 1까지 모두 흰칸(1)이 아니면 중단
                # 중단이후 다음 x 좌표로
                for i in range(k):
                    if arr[y][x + i] != 1:
                        break
                # x -> x + k - 1까지 모두 흰칸(1)이고
                else:
                    # x 가 0이라면 :
                    # x + k 번째 자리 (단어 길이 + 1) 가 검은칸(1)이면 count += 1
                    if x == 0:
                        if arr[y][x + k] == 0:
                            cnt += 1
                    # 0< x < n - k 이라면 :
                    # x -1 번째 자리 (단어 시작지점 - 1) 와
                    # x + k 번째 자리 (단어 끝지점 + 1) 가 검은칸(1)이면 count += 1
                    elif x < n - k:
                        if arr[y][x + k] == 0 and arr[y][x - 1] == 0:
                            cnt += 1
                    # x + k가  n 이라면 :
                    # x -1 번째 자리 (단어 시작지점 - 1)가 검은칸(1)이면 count += 1
                    elif x + k == n:
                        if arr[y][x - 1] == 0:
                            cnt += 1
        return cnt

    n, k = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]
    count = 0

    # N x N 행렬이므로 전치 이후 가로 길이 검사 시
    # 가로 세로 모두 검사 가능
    transposed = list(zip(*arr))
    count += k_length_word(arr)
    count += k_length_word(transposed)

    print(f"#{tc}", count)




