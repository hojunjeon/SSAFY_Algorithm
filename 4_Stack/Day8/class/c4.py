# 약수들의 합

import sys
sys.setrecursionlimit(10**6)


# 시작값: 1
# 끝점 : N // 2
# num: 1씩 증가하는 숫자, acc_list : 약수 리스트
def recur(num, acc_list):
    if num > N // 2:
        return acc_list
    
    # 약수 체크
    if N % num == 0:
        acc_list.append(num)
    
    return recur(num + 1, acc_list)


while True:
    N = int(input())

    if N == -1:
        break

    divisors = recur(1, [])

    if sum(divisors) == N:
        print(f'{N} = {" + ".join(map(str, divisors))}')
    else:
        print(f'{N} is NOT perfect.')