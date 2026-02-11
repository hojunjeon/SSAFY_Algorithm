# 계산기1
# 연산자가 + 하나 일 때


def infix_to_postfix(tokens):
    result = []
    oper_stack = []

    # 1. 숫자면 그대로 result 에 쌓는다
    # 2. 연산자라면
    #   - oper_stack 이 비어있을 때: oper_stack 에 추가
    #   - 아닐 때
    #     - 나보다 우선순위가 크거나 같은 연산자들을 result 로 이동 후 추가

    for token in tokens:
        if token.isdigit():
            result.append(token)
        else:
            if oper_stack:
                result.append(oper_stack.pop())

            oper_stack.append(token)

    result.append(oper_stack.pop())  # 남은 연산자 하나

    return result


def get_result(tokens):
    stack = []
    # 숫자라면 그냥 stack 에 넣기
    # 연산자라면, stack 에서 숫자 2개 꺼내서 계산 후 다시 넣기
    for token in tokens:
        if token.isdigit():
            # 계산하기 위해서 int 로 변환하여 넣자
            stack.append(int(token))
        else:
            num1 = stack.pop()
            num2 = stack.pop()

            stack.append(num1 + num2)

    return stack[0]


for tc in range(1, 11):
    N = int(input())
    row = input()
    postfix = infix_to_postfix(row)  # 후위 표기법 으로 변환
    result = get_result(postfix)     # 계산
    print(f'#{tc} {result}')