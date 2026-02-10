# 문제집 공유용 재귀 10829 이진수 변환

n = int(input())

result = []

while n > 0 :
    r = n %2
    n //= 2
    result.append(r)
result = result[::-1]

print(''.join(map(str, result)))

def recur(n):
    if n == 0:
        return
    r = n % 2 # 10 = 0 1 0 1
    recur(n // 2)
    print(r, end='')


recur(n)