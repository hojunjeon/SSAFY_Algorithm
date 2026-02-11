# 콜라츠 추측 정답 코드

import sys
sys.stdin = open("input.txt", "r")


# 재귀호출 구조
# - 시작: N
# - 끝: 1
# - 누적값(파라미터): 계산된 값
def recur(num):
    global cnt

    # num 이 1 이면 끝
    if num == 1:
        return

    cnt += 1

    # num 가 짝수면
    if num % 2 == 0:
        recur(num // 2)
    # num 가 홀수면
    else:
        recur(num * 3 + 1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    recur(N)
    print(f'#{tc} {cnt}')