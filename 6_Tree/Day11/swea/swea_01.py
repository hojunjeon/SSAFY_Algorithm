# swea Tree1 [S/W 문제해결 기본] 9일차 - 중위순회 

import sys
sys.stdin = open('02_SSAFY_Algorithm\\6_Tree\swea\input.txt', 'r')

# T = int(input())
T = 10

def inorder(node, root, edge):
    if root != None:    
        if edge[root][0] == None and edge[root][1] == None:
            print(node[root], end ='')
            return
        
        inorder(node, edge[root][0], edge)
        print(node[root], end='')
        inorder(node, edge[root][1], edge)
        return 
    

for tc in range(1, 10 + 1):
    n = int(input())
    edge = [[None, None] for _ in range(n + 1)]
    node = [0]
    
    for i in range(1, n + 1):
        temp = list(input().split())
        node.append(temp[1])
        for j in range(2, len(temp)):
            edge[i][j-2] = int(temp[j])
    
    print(f'#{tc} ', end = '')
    inorder(node, 1, edge)
    print()
    