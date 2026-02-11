# [S/W 문제해결 기본] 10일차 - 비밀번호 문제 정답

import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    arr = input().split()
    stack = []
    
    # 숫자를 보고
    # - 저장되어 있는 곳(==stack)의 마지막 숫자와 현재 숫자 비교

    for num in arr[1]:
        # 1. stack 이 비어있으면, 그냥 숫자를 stack 에 넣는다
        if len(stack) == 0:
            stack.append(num)
        # 2. stack 의 마지막 데이터와 현재 숫자를 비교한다.
        #   - 같다면, stack 의 마지막 숫자를 제거
        #   - 다르다면, stack 에 숫자를 추가
        else:
            if num == stack[-1]:
                stack.pop()
            else:
                stack.append(num)

    print(f'#{tc} {"".join(stack)}')