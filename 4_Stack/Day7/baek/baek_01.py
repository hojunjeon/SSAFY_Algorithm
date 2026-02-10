# 스택과제공지 10870 피보나치수5

fib_list = [0, 1]

def fibo_recur(n):
    if n <= 1:
        return n
        
    else:
        return fibo_recur(n-1) + fibo_recur(n-2)
    

def fibo_memo(n):
    global fib_list
    if n <= 1:
        return n
    else:
        fibo_memo(n - 1)
        fib_list.append(fib_list[n - 1] + fib_list[n -2])
        return fib_list
    
n = int(input())

result_recur = fibo_recur(n)
result_memo = fibo_memo(n)

print(result_recur)
print(result_memo[n])