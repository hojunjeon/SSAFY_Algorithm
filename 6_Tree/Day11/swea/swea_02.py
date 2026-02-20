# swea Tree1 [파이썬 S/W 문제해결 기본] 8일차 - subtree

import sys
sys.stdin = open('02_SSAFY_Algorithm\\6_Tree\swea\input.txt', 'r')

T = int(input())

def pre(root, cnt):
    if root == 0:
        return cnt

    cnt += 1
    cnt = pre(node[root][0], cnt)
    cnt = pre(node[root][1], cnt)

    return cnt

for tc in range(1, T + 1):
    e, root = map(int, input().split()) # 노드의 갯수 = 간선의 갯수 + 1
    edge = list(map(int, input().split()))
    node =[[0,0] for _ in range(e + 2)]
    
    for i in range(e):
        par, chi = edge[i*2], edge[i*2+1]
        if node[par][0] == 0:
            node[par][0] = chi
        else: node[par][1] = chi
        
    cnt = pre(root, 0)
    
    print(f'#{tc} {cnt}')