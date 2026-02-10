# 문제집공유용 5.재귀 9506 약수들의합
import sys
sys.setrecursionlimit(10**6)

n = int(input())
m_list = []

def measure(n, m_list):
    if n <= 1 :
        return

    for i in range(2, n + 1):
        if n % i == 0 and i not in m_list:
            m_list.append(i)
            print(n, i, m_list)
            measure(n // i, m_list)

            
    return 

lst = []
lst = measure(n, lst)
print(lst)



