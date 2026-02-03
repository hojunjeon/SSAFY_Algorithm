T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    max_sum = 0
    min_sum = 9999999999999999999
    sum_list = []

    for i in range(0, N - M + 1):
        sum_m = 0

        for j in range(M):
            sum_m += num_list[i+j]

    # 1. 내장함수 X
    #
    #     if sum_m > max_sum:
    #         max_sum = sum_m
    #     if sum_m < min_sum:
    #         min_sum = sum_m
    #
    #     # print(max_sum, min_sum)
    #
    #================================

    # 2. 내장함수 O
        sum_list.append(sum_m)

    max_sum = max(sum_list)
    min_sum = min(sum_list)

    print(f'#{tc} {max_sum - min_sum}')
