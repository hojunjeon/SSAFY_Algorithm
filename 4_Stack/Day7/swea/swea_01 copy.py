import sys
sys.stdin = open('SSAFY_Algorithm\\4_Stack\Day7\swea\input.txt','r')

T = int(input())
 
def dfs(st):
    global li
    print(st, end = " ")
    for i in range(N):
        if i not in li and number[st][i] == 1:
             
            li += [i]
            dfs(i)

    return

for c in range(T):
    N = int(input())
    number = [list(map(int, input().split())) for _ in range(N)]
    print(number)
    print(f'#{c+1}', end = " ")
    li = [0]
    dfs(0)

    print("")