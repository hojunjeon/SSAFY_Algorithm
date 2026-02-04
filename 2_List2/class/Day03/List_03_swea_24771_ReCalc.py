import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    ### 실패 : 시간 초과 -> O(n^2) ###
    '''
    # n : 고객수 / arr : 고객 요금 / p : 이벤트 수 / event : 각 이벤트 배열
    # 1. event[0] ~ event[p-1] 하나씩 순회
    #     - 1. start = event[y][0] / end = event[y][1] / price = event[y][2]
    #     - 2. arr을 순회하며 
    #         - 1) start <= i <= end 일 때 : arr[i] += price 
    '''

    ### 누적합 사용 O(p + n) ###
    '''
    1. event를 순회하며 charge_list (요금 부과 리스트 ) 생성 -> 누적합을 위한 리스트
        - charge_list[start] += price
        - charge_list[end + 1] -= price
    2. arr을 순회하며 같은 인덱스의 charge_list value를 부과
        - 누적합을 사용하여 charge_list[i] += charge_list[i-1]
    '''

    n = int(input())
    arr = list(map(int, input().split()))

    p = int(input())
    events = [list(map(int, input().split())) for _ in range(p)]

    # 최대 100,000 + 100,000
    charge_list = [0] * (n + 1)

    for start, end, price in events:  # 최대 100,000
        charge_list[start] += price
        charge_list[end + 1] -= price
        # [3, 3, 3, 0, 0, 0]
        # [0, -1, -1, -1, -1, 0]
        # [3, -1, 0, -3, 0, 1]

    add = 0
    # 최대 100,000
    for i in range(n):
        add += charge_list[i]
        # [3, 2, 2, -1, -1, 0]
        arr[i] += add

    result = ' '.join(map(str, arr))
    print(f'#{tc} {result}')
