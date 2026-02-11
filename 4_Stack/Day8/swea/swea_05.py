# swea 스택과재귀2 [S/W 문제해결 기본] 6일차 - 계산기 2
'''
# 중위표기 -> 후위 표기
1. token이 숫자이면 result에 push
2. token이 닫는 괄호) 이면
    - 1. 여는 괄호가 나올 때까지 result.append(stack.pop())
3. 스택이 비어있으면 token push
4. token이 연산자이면
    - 1. token 보다 priority가 낮은 stack[-1]이 나올 때 까지 result.append(stack.pop())
5. 반복 종료 이후 남은 stack 전부 pop해서 result에 push
'''
# 5 + 4 * 2 = 542*+
# 5 + 7 / 4 * 2 = 574/+2*

import sys
sys.stdin = open('02_SSAFY_Algorithm\\4_Stack\Day8\swea\input.txt','r')

for tc in range(1, 11):
    n = int(input())
    tokens = list(input())

    stack=[]
    result=[]
    priority = {'(' : 3, '*' : 2, "+" : 1}

    # 중위 -> 후위 표기식으로 변환 
    for token in tokens:
        if token.isdigit():
            result.append(token)

        elif token == ')':
            while stack[-1] == '(':
                result.append(stack.pop())
            stack.pop()

        elif not stack:
            stack.append(token)
        else:
            while stack and priority[token] <= priority[stack[-1]]:
                result.append(stack.pop())
            stack.append(token)
    
    while stack:
        result.append(stack.pop())



    # 후위 표기식 계산 과정
    stack1 = []

    for token in result:
        if token.isdigit():
            stack1.append(int(token))
            continue

        t1 = stack1.pop()
        t2 = stack1.pop()

        if token == "*":
            
            stack1.append(t1 * t2)

        elif token == "+":
            stack1.append(t1 + t2)

    print(f"#{tc} {stack1[0]}")