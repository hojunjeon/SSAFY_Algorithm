# swea 스택과재귀2 [S/W 문제해결 기본] 6일차 - 계산기


import sys
sys.stdin = open('02_SSAFY_Algorithm\\4_Stack\Day8\swea\input.txt','r')

for tc in range(1, 11):
    n = int(input())
    tokens = list(input())

    stack=[]
    result=[]

    for token in tokens:
        if token.isdigit():
            result.append(token)
        elif not stack:
            stack.append(token)
        else:
            result.append(token)

    result.append(stack.pop())

    stack1 = []
    result1 = []
    for token in result:
        if token.isdigit():
            stack1.append(int(token))
        else:
            t1 = stack1.pop()
            t2 = stack1.pop()

            stack1.append(t1 + t2)

    print(f"#{tc} {stack1[0]}")