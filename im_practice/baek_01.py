# 문제집공유용 10. 시크릿 문제집 5397 - 키로거

# 실패 1 : password가 비었을 때, '-'입력 시 index오류 남
# -> '-'가 입력되었을 때 top > 0이면 동작

T = int(input())

for tc in range(1, T + 1):
    l = list(input())
    password = []
    top = 0

    for i in range(len(l)):
       
        if l[i] == "<":
            if top > 1:
                top -= 1

        elif l[i] == ">" :
            if top < len(password):
                top += 1
            
        elif l[i] == '-':
            if top > 0:
                top -= 1
                password.pop(top)

        else:
            password.insert(top, l[i])
            top += 1

    print(''.join(password))