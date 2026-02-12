# swea 스택과재귀2 장훈이의 높은 선반

import sys
sys.stdin = open('02_SSAFY_Algorithm\\4_Stack\Day9\swea\input.txt', 'r')


n,b = map(int, input().split())
arr = list(map(int, input().split()))

def tower(idx, subset):

    if  idx == len(arr):
        print(subset)
        return

    # if sum(subset) < b:
    #     return

    
    # 1. 현재 원소를 부분집합에 포함 O
    subset.append(arr[idx])
    tower(idx + 1, subset)
    subset.pop()

    #2. 현재 원소를 부분집합에 포함 X
    tower(idx + 1, subset)

tower(0,[])