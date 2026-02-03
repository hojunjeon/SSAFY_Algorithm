T = int(input())

for tc in range(1, T+1):

    '''
    1. card에 입력받은 list()를 이용해 한 글자식 문자열로 저장
    2. card를 순회하며 해당하는 값의 count를 1증가
    3. count의 max_value를 찾고 해당 인덱스를 찾아냄 
    '''

    n = int(input())
    card = list(input())

    count = [0] *(10)

    for i in range(n):
        count[int(card[i])] += 1

    # max_count = 0
    #
    # for i in range(len(count)-1, -1, -1):
    #     if count[i] > max_count:
    #         max_count = count[i]
    #         high = i

    max_val = max(count)
    high = max([i for i, x in enumerate(count) if x == max_val])


    print(f'#{tc} {high} {count[high]}')
