# [S/W 문제해결 기본] 10일차 - 비밀번호
import sys
sys.stdin = open('SSAFY_Algorithm\\4_Stack\Day6\input.txt','r')

T = 10

for tc in range(1, T + 1):


    n, password = input().split()
    n = int(n)
    password = list(password)

    # ===========================================
    # 1. 리스트 메서드로 구현

    stack = []

    for i in range(n):
        if stack :
            if stack[-1] == password[i] :
                stack.pop()

            else :
                stack.append(password[i])
        else:
            stack.append(password[i])

    print(f"#{tc} {''.join(map(str,stack))}")
    # ===========================================


    # =========================================
    # 2. 리스트 인덱스로 구현

    # top = -1
    # stack = [None] * n

    # for i in range(n):
    #     top += 1

    #     if stack[top -1] == password[i]:
    #         top -= 2
    #         stack[top + 1] = None         

    #     else:
    #         stack[top] = password[i]        

    # print(f"#{tc} {''.join(stack[:top+1])}")
    # ===========================================
