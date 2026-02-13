from collections import deque
from pprint import pprint

n, m, v = map(int, input().split())

# 인접 행렬
adj_arr = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    
    adj_arr[start][end] = 1
    adj_arr[end][start] = 1

def bfs(v):
    dq = deque([v])  # 방문 예약
    visited = [0] * (n + 1) # 방문 목록
    print(v, end =' ')
    visited[v] = 1

    
    # 방문 예약 목록이 빌 때까지
    while dq:
        now = dq.popleft()
        
        # 현재 노드에 연결된 노드들 중 아직 방문하지 않은( visited[i] == 0인 ) 노드들을 방문 예약 목록 dq에 append
        for i, val in enumerate(adj_arr[now]):
            # 현재 노드에서 i노드까지 경로가 있고
            # i노드를 아직 방문하지 않았다면
            if val == 1 and visited[i] == 0:
                # dq에 append와 동시에 방문을 기록 
                # -> 다음 while 문에서 어짜피 방문할 것이기 때문
                print(i, end = ' ')
                visited[i] = 1
                dq.append(i)
    print()


# def dfs(v):

#     new_arr = []
#     for i in range(n+1):
#         new_arr.append(adj_arr[i][:])
    
#     stack = [v]
#     visited = [0] * (n + 1) # 방문 목록
#     print(v, end = ' ')
#     visited[v] = 1
    
#     while stack:
#         now = stack.pop()
            
        
#         for i, val in enumerate(new_arr[now]):
#             if val == 1 and visited[i] == 0:
#                 print(i, end = ' ')
#                 new_arr[now][i] = 0
#                 visited[i] = 1
#                 stack.append(i)
#                 break
        
#     print()
    
def dfs(v):
    print(v, end = ' ')
    visited[v] = 1

    for next in range(1, n+1):
        if adj_arr[v][next] == 0 or visited[next] == 1:
            continue
        dfs(next)

visited = [0] * (n + 1) # 방문 목록

dfs(v)
print()
bfs(v)

