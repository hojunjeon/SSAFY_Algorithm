# swea 스택과재귀2 [S/W 문제해결 기본] 6일차 - 계산기 3
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

import sys
sys.stdin = open('02_SSAFY_Algorithm\\4_Stack\Day8\swea\input.txt','r')

for tc in range(1, 11):
    n = int(input())
    tokens = list(input())

    stack=[]
    result=[]
    priority = {'*' : 2, "+" : 1}

    # 중위 -> 후위 표기식으로 변환 
    for token in tokens:
        
        # 숫자 입력 시 result에 push
        if token.isdigit():
            result.append(token)

        # 여는 괄호 들어오면 stack에 push
        elif not stack or token == '(':
            stack.append(token)

        # 닫는 괄호 들어오면 여는 괄호 나올 때 까지 result에 stack.pop() push
        elif token == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

        # 연산자 들어왔을 때 
        else: 
            while True:
                if stack[-1] != "(" and priority[token] <= priority[stack[-1]]:
                    result.append(stack.pop())
                else:
                    stack.append(token)
                    break
    # 모든 토큰 확인 이후 stack에 남은 토큰 result에 pop해서 push
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