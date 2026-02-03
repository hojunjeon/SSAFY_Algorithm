T = int(input())

for tc in range(1, T+1):

    '''
    1. num_list를 순회하며
        -1. num_list[i] >= num_list[high] 이면  # 동일값이면 오른쪽 인덱스
            high = i
        -2. num_list[i] < num_list[low] 이면   # 동일값이면 왼쪽 인덱스
            low = i               
            
    2. abs(high - low)
    '''
    n = int(input())
    num_list = list(map(int, input().split()))

    high = n-1
    low = 0

    for i in range(n):
        if num_list[i] >= num_list[high]:
            high = i
        if num_list[i] < num_list[low]:
            low = i

    print(f'#{tc} {abs(high - low)}')