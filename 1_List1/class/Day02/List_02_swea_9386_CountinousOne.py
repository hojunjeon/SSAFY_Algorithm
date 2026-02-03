T = int(input())

for tc in range(1, T + 1):
    '''
    1. num_list를 순회하며 
        - 1. num_list[i] == 1 이면
            count += 1
            - max_count < count 면
                max_count = count
                
        - 2. num_list[i] == 0 이면
            count = 0
            
    '''
    n = int(input())
    num_list = list(input())

    max_count = 0
    count = 0

    for num in num_list:
        if num == '1':
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 0

    print(f'#{tc} {max_count}')