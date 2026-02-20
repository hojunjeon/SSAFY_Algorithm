# 문제집공유용 10. 시크릿 문제집 5397 - 키로거

# 실패 1 : password가 비었을 때, '-'입력 시 index오류 남
# -> '-'가 입력되었을 때 top > 0이면 동작

# 실패 2 : top의 위치에서 pop과 insert를 진행 시 top 뒤쪽 인덱스는 전부 움직여야하는 문제 발생 -> 비효율적
# -> left와 right 리스트로 관리

T = int(input())

for tc in range(1, T + 1):
    
    ''' # 실패 2
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
    '''
    
    l = list(input())
    left = []
    right = []
    
    for i in range(len(l)):
        data = l[i]
        if data == "<":
            if left:
                right.append(left.pop())
            else:
                continue
        
        elif data == ">":
            if right:
                left.append(right.pop())
            else:
                continue
            
        elif data == "-":
            if left:
                left.pop()
            else:
                continue
            
        else:
            left.append(data)
            
    print(''.join(left)+''.join(right[::-1]))