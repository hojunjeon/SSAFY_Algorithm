# 스택과제공지 24416 피보나치수1

cnt_recur = 1
cnt_dp = 0

def fib(n):
    global cnt_recur
    if n == 1 or n == 2:
        return 1;  # 코드1
    else:
        cnt_recur += 1
        return (fib(n - 1) + fib(n - 2))

def fibonacci(n):
    global cnt_dp
    f = [0] * (n+1)
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        cnt_dp += 1
        f[i] = f[i - 1] + f[i - 2]  # 코드2
    return f[n]

n = int(input())

fib(n)
fibonacci(n)
print(cnt_recur, cnt_dp)
