# 피보나치수

# 기본 재귀 호출

# fibo(10) = fibo(9) + fibo(8)
def fibo(num):
    if num <= 1:
        return num

    return fibo(num - 1) + fibo(num - 2)

N = int(input())
result = fibo(N)
print(result)


# 메모이제이션

# fibo(10) = fibo(9) + fibo(8)
def fibo(num):
    if num <= 1:
        return num

    if memo.get(num):       # 계산한 적이 있다면
        return memo[num]    # 기존 기록된 값을 return

    # 한 번이라도 연산했다면, 딕셔너리에 기록
    memo[num] = fibo(num - 1) + fibo(num - 2)
    return memo[num]

N = int(input())
memo = {}
result = fibo(N)
print(result)


# DP 활용

N = int(input())
mod = 1000000007
fibo = [0] * 1000001
fibo[0] = 0  # 초기값
fibo[1] = 1  # 초기값

# 세 번째 수부터는 이전의 값들을 활용할 수 있다
for i in range(2, 1000001):
    fibo[i] = (fibo[i-1] + fibo[i-2]) % mod

print(fibo[N])