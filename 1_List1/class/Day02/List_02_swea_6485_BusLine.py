# import sys
#
# sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    '''
    0. count_list 의 index : 정류장 번호 / value : 정류장을 지나는 노선의 개수
    1. a, b를 입력받아 range(a, b+1) -> a이상 b이하의 정류장 (count_list) 1씩 증가
    2. c_list를 입력받고 하나씩 순회하며 해당 정류장을 지나는 노선의 개수를 출력
    '''

    n = int(input())
    count_list = [0] * 5002

    for _ in range(n):
        a, b = map(int, input().split())
        count_list[a] += 1
        count_list[b+1] -= 1

    for i in range(1, 5001):
        count_list[i] += count_list[i-1]


    p = int(input())
    c_list = [int(input()) for _ in range(p)]

    print(f'#{tc}', end = ' ')
    print(' '.join(str(count_list[c]) for c in c_list))
