# swea 스택과재귀1 [S/W 문제해결 기본] 4일차 - 괄호 짝짓기
'''
1. ch가 닫는 괄호 아닐 때 -> )}]>
    - ch를 stack에 추가
2. ch 닫는 괄호 일 때 
    - stack[-1]과 짝이면 pop
3. 반복 종료 이후 stack에 여는 괄호가 남아있으면 0 / 비었으면 1
'''

import sys
sys.stdin = open('02_SSAFY_Algorithm\\4_Stack\Day8\swea\input.txt','r')

for tc in range(1, 11):
    n = int(input())
    s = list(input())
    stack = []

    pair = { '(':')', '{':'}', '[':']', '<':'>' }

    for ch in s:

        if not stack or ch not in pair.values():
            stack.append(ch)
        elif pair[stack[-1]] == ch:
            stack.pop()
        else:
            break

    if stack :
        print(f"#{tc} 0")
    else:
        print(f"#{tc} 1")
