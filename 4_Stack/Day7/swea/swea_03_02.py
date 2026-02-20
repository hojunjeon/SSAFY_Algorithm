# swea 스택과재귀 파스칼삼각형
import sys
sys.stdin = open('SSAFY_Algorithm\\4_Stack\Day7\swea\input.txt','r')

tc, n = map(int, input().split())

a = list(map(int, input().split()))

way_dict = {}

i = 0
b = [[0] for _ in range(100)]

while i < n:
    s , e = a[i*2], a[i*2 + 1]

    b[s].append(e)
    i += 1

stack = []
way = []

def dfs(n):
    num = b[n].pop()

    # 경로 없을 때
    if num == 0 :
        k = way.pop()
        
        return 
    if num == 99:
        return way
    
    else:
        for i in range(len(b[n])):
            b[n][i]
