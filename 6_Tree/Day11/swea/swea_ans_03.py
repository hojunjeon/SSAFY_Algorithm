# swea Tree1 그래프마스터 - 효정이의 크리스마스 트리 정답
# 전위순회
def recur(node):
    # 자식이 없다면 되돌아가자
    if node == -1:
        return

    # print(node, end=' ')  # 현재 노드를 출력 (전위순회)
    preorder.append(node)

    recur(graph[node][0])  # 왼쪽 자식으로 이동

    # print(node, end=' ')  # 현재 노드를 출력 (중위순회)
    inorder.append(node)

    recur(graph[node][1])  # 오른쪽 자식으로 이동

    # print(node, end=' ')  # 현재 노드를 출력 (후위순회)
    postorder.append(node)



T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [[] for _ in range(N + 1)]  # 인접리스트

    for _ in range(N):
        node, left, right = map(int, input().split())
        graph[node].append(left)
        graph[node].append(right)

    # 순회 결과를 저장할 리스트
    preorder = []
    inorder = []
    postorder = []

    recur(1)
    print(f'#{tc}')
    print(*inorder)
    print(*preorder)
    print(*postorder)