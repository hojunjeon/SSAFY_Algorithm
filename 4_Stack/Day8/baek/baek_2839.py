# 문제집공유용 2.그리디 2839 설탕 배달 

number = int(input())

def solve(n):
    '''
    1. n >= 일 때 까지 반복
     - 1. n 이 5로 나누어 떨어지면
        즉시 5로 나눈 몫(개수)를 현재 cnt에 더하고 return
     - 2. 나누어 떨어지지 않으면 n -3 이후 cnt ++ 하고 다음 반복
    2. 반복 이후 나누어 떨어지지 않으면 -1 return
    '''
    bags = 0
    while n >= 0:
        if n % 5 == 0:
            bags += n // 5
            return bags
        n -= 3
        bags += 1
    return -1


print(solve(number))
