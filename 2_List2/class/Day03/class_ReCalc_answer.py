import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    delta = [0] * (N + 1)  # 마지막 인덱스는 버린다

    P = int(input())
    for _ in range(P):
        start, end, cost = map(int, input().split())
        delta[start] += cost
        delta[end + 1] -= cost

    current_delta = 0  # 현재 시점의 변화량
    for i in range(N):
        current_delta += delta[i]  # 누적
        arr[i] += current_delta

    print(f'#{tc}', *arr)
    # [참고] f-string 안에 넣고싶다면 아래와 같이 join 활용
    # print(f'#{tc} {" ".join(map(str, arr))}')