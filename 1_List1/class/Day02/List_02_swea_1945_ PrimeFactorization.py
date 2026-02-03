# import sys
#
# sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    '''
    1. 소수리스트 요소를 하나씩 순회하며 지수 증가 여부 체크
        - 1. n을 prime_list[i]로 나눈 나머지가 0이면
            factor[i] += 1
        ~ 1. 나머지가 0이 아니라면 = 소수가 아니라면
            break
        
    '''
    prime_list = [2, 3, 5, 7, 11]
    n = int(input())
    factor = [0] * 5

    for i in range(len(prime_list)):
        while True:
            if n % prime_list[i] == 0:
                factor[i] += 1
                n //= prime_list[i]
            else:
                break

        if n == 1:
            break

    print('#'+str(tc), factor[0], factor[1], factor[2], factor[3], factor[4])