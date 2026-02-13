# BFS 기초

import sys
sys.stdin = open('02_SSAFY_Algorithm\\5_Queue\input.txt','r')

from collections import deque

n, m = map(int, input().split())

# 빈 인접 리스트 생성
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    
print(graph)


def bfs(start):
    # 초기화
    dq = deque([start])
    visited = [0] * (n + 1)
    visited[start] = 1
    print(start, end = ' ')

    while dq:
        now = dq.popleft()
        # print(now, end=' ')
        
        for next in graph[now]:
            if visited[next]:
                continue
            print(next, end = ' ')
            visited[next] = 1
            dq.append(next)
            
bfs(1)