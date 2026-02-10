'''
7 7
1 2 1 3 2 4 2 5 4 6 5 6 6 7
'''
def dfs(v, N):            # v출발, N마지막 정점
    visited = [0] * (N + 1)    # 방문표시
    stack = []                  # 스택

    stack.append(v)

    while stack:
        node = stack.pop()
        if visited[node] != 1:
            visited[node] = 1
            print(node)
            stack.extend(adj_list[node])



V, E = map(int, input().split())
graph = list(map(int, input().split()))
adj_list = [[] for _ in range(V+1)]         # 인접 리스트
for i in range(E):
    v, w = graph[i*2], graph[i*2+1]     #

    adj_list[v].append(w)
    adj_list[w].append(v)                 # 방향이 없는 경우

dfs(1, V)                           # 1번부터 탐색색