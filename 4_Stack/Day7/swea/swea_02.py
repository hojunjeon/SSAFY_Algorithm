# swea 스택과재귀 파스칼삼각형
import sys
sys.stdin = open('SSAFY_Algorithm\\4_Stack\Day7\swea\input.txt','r')

T = int(input())

def pascal(n):
    '''
    i : 0 -> n
        1. arr[i][0] , arr[i][i] = 1
        2. arr[i][x] = arr[i-1][x-1]+arr[i-1][x]

    # 각y의 마지막 요소 (x==y) : 1
    '''
    global arr

    for y in range(1, n):
        for x in range(1, y + 1):
            if x == y:
                arr[y].append(1)
                continue
            arr[y].append(arr[y-1][x-1] + arr[y-1][x])

 
for tc in range(1, T + 1):
    n = int(input())
    arr = [[1] for _ in range(n)]

    pascal(n)
    print(f"#{tc}")
    for row in arr:
        print(*row)