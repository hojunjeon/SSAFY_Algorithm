# DFS
'''
입력

6 7
1 2
1 3
1 4
2 4
2 5
4 5
4 6

'''

import sys
sys.stdin = open("input.txt", "r")


# 시작점: 1번 node
# 종료지점: 갈 수 있는 모든 노드를 방문했을 때
def dfs(node):
    print(node, end=' ')  # 현재 방문한 노드를 출력

    # 현재 node 로 부터 갈 수 있는 노드들을 방문
    # 전체 노드를 확인
    for next_node in range(1, N + 1):
        # 갈 수 없는 노드는 pass
        if graph[node][next_node] == 0:
            continue

        # 이미 방문한 노드라면 pass
        if visited[next_node]:
            continue

        visited[next_node] = 1  # 방문 처리
        dfs(next_node)  # 다음 노드로 이동

# 정점 수, 간선 수
N, M = map(int, input().split())

# 인접 행렬
# - 0번은 버린다고 가정하고, 7*7로 생성
graph = [[0] * (N + 1) for _ in range(N + 1)]
# 방문여부를 기록
visited = [0] * (N + 1)

# 그래프 연결
for _ in range(M):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1  # 양방향 그래프

visited[1] = 1
dfs(1)
