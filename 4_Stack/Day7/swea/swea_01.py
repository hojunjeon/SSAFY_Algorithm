# swea 스택과재귀1  DFS 기초 - 방문 순서 출력하기
# 초안
from pprint import pprint


import sys
sys.stdin = open('SSAFY_Algorithm\\4_Stack\Day7\swea\input.txt','r')

def dfs(graph) :
    '''
    0 - 2 3 4 / 2 - 5 6 
    스택에 노드0를 넣고 / 방문에 노드0를 넣고 
    [0] [0]
    노드0에 연결된 첫번째 자식노드2를 부모노드로2
    node = 2

    스택에 노드2를 넣고 / 방문에 노드2를 넣고
    [0 2][0 2]
    노드2에 연결된 첫번째 자식노드5를 부모노드로5
    node = graph[node2].pop(0) = 5

    스택에 노드5를 넣고 / 방문에 노드5를 넣고
    [0 2 5][0 2 5]
    노드5에 연결된 자식노드가 없으면
        stack.pop()  -> 5
        [0 2][0 2 5]
        node = stack[-1]
        node = 2

    스택에 노드2가 있으니 pass / 방문에 노드 2가 있으니 pass
    [0 2][0 2 5]
    노드2에 연결된 첫번째 자식노드6를 부모노드로6
    node = graph[node2].pop(0) = 6
    
    스택에 노드6 넣고 / 방문에 노드6 넣고
    [0 2 6][0 2 5 6]
    노드6에 연결된 자식 노드가 없으면
        stack.pop() -> 6
        [0 2][0 2 5 6]
        node = stack[-1]
        node = 2

    스택에 노드2가 있으니 pass / 방문에 노드 2가 있으니 pass
    [0 2][0 2 5 6]
    노드2에 연결된 자식 노드가 없으면 graph[node] == []
        stack.pop() -> 2
        [0][0 2 5 6]
        node = stack[-1]
        node = 0

    스택에 노드0가 있으니 pass / 방문에 노드 0가 있으니 pass
    [0][0 2 5 6]
    노드0에 연결된 첫번째 자식노드3를 부노노드로3
    node = 3
    '''
    stack = []
    visited = []
    stack.append(0)
    node = 0

    while True:
    
        if node not in stack:
            stack.append(node)
        if node not in visited:
            visited.append(node)

        if not graph[node]:
            stack.pop()
            if stack:
                node = stack[-1]
                continue
            else:
                break

        if graph[node][0] in visited:
            tnode = node
            for _ in range(len(graph[tnode])):
                node = graph[tnode].pop(0)
                if node not in visited:
                    break       

            else:
                stack.pop()
                if not stack:
                    break
                node = stack[-1]

        else:
            node = graph[node].pop(0)

    return visited

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    graph = {}


    temp = [list(map(int, input().split())) for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if temp[y][x] == 1:
                graph.setdefault(y,[]).append(x)
                graph.setdefault(x,[]).append(y)
    visited = dfs(graph)
    print(f"#{tc} {' '.join(map(str, visited))}")
