# swea 스택과재귀1 [S/W 문제해결 기본] 4일차 - 길찾기

import sys
sys.stdin = open('02_SSAFY_Algorithm\\4_Stack\Day8\swea\input.txt','r')

for _ in range(10):
    tc, n = map(int, input().split())
    a = list(map(int, input().split()))

    i = 0
    b = [[0] for _ in range(100)]
    # b = {}

    while i < n:
        s , e = a[i*2], a[i*2 + 1]

        b[s].append(e)
        # b.setdefault(s, []).append(e)
        i += 1

    stack = []
    visited = []

    def dfs(n):
        global visited
        '''
        1. 노드 방문 visited.append(n)
        1. 연결된 노드가 없을 시 -> if b[n][-1] == 0:
            - 이전 노드로 돌아가기 위해 경로에서 현재 노드 제외 -> visitied.pop()
            - 이전 노드로 돌아감 -> return
        2. 연결된 노드가 있을 시 -> else:
            - 노드에 연결 된 간선의 수 만큼 반복(2) -> for _ in range(2):
                - 현재 노드와 연결된 노드 -> num = b[n].pop()
                - 연결된 노드로 dfs -> r = dfs(num)
                - return 된 값에 따라 다음 행동
                    1 ) r = None (연결된 노드가 없어 이전 노드로 돌아온 경우):
                        현재 노드에서 연결된 다음 노드로 dfs
                    2 ) r = 1 (이전 노드가 도착지99 인 경우):
                        계속 1을 return 해 재귀 함수 전체적으로 종료 하도록 함
                    3 ) r = None 이고 이전 노드에 연결된 노드가 없을 때 (길이 아닐 때):
                        한번 더 이전 노드로 돌아감 -> visited.pop()
        3. if num == 99 : return list
        '''
        visited.append(n)
        if n == 99 :
            return 1
        if b[n][-1] == 0:
            visited.pop()
            return
        
        else:
            while True:
                num = b[n].pop()
                r = dfs(num)
                if r == None and b[n][-1] == 0:
                    visited.pop()
                    return
                if r == 1:
                    return 1    

    dfs(0)
    if not visited:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} 1")
