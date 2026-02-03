T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    for i in range(N-1, -1, -1):
        for j in range(i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    print(f'#{tc} {num_list[-1] - num_list[0]}')