# swea 스택과재귀1  DFS 기초 - 방문 순서 출력하기

import sys
sys.stdin = open('SSAFY_Algorithm\\4_Stack\Day7\swea\input.txt','r')

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)
            
T = int(input())
for w in range(1,T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    stack = {}
    visited = [False]*N
    graph = [[] for _ in range(100)]
    for a in range(N):
        for b in range(N):
            if data[a][b] ==1: 
                graph[a].append(b)
    print(f'#{w}', end=' ')
    dfs(0)
    print()