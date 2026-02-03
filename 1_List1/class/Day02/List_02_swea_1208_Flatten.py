T = 10

for tc in range(1, T + 1):
    '''
    # dump 횟수
    # DATA : 상자 높이 리스트
    # COUNT : 상자 높이 갯수 리스트
    # TEMP : 정렬 완료 된 리스트
    1. dump 횟수 만큼 상자 옮기기 반복
        - 1. COUNT[[HIGH]가 0일 경우
            - HIGH -= 1
        - 2. COUNT[LOW]가 0일 경우
            -LOW += 1
        - 3. COUNT[HIGH] -= 1 / COUNT[HIGH-1] += 1
        - 4. COUNT[LOW] -= 1 / COUNT[LOW+1] += 1
    
    '''
    dump = int(input())
    data = list(map(int, input().split()))
    count = [0] * ( 101 )
    temp = []

    # data의 각 원소를 카운팅
    for d in data:
        count[d] += 1

    # 가장 큰 수 인덱스 high 찾기
    high = len(count) -1
    while True:
        if count[high] != 0:
            break
        high -= 1

    # 가장 작은 수 인덱스 low 찾기
    low = 0
    while True:
        if count[low] != 0:
            break
        low += 1

    # dump 만큼 반복
    for i in range(dump):

        count[high] -= 1
        count[high - 1] += 1
        count[low] -= 1
        count[low + 1] += 1

        if count[high] == 0:
            high -= 1
        if count[low] == 0:
            low += 1

    # 모든 반복 이후 마지막 요소가 0인지 확인해 high와 low 조절
    if count[high] == 0:
        high -= 1
    if count[low] == 0:
        low += 1

    print(f'#{tc} {high - low}')