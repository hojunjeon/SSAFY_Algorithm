import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    '''
    # ========================
    # Pass_01 
    1. 알파뱃의 개수 만큼의 0리스트 생성
    2. 입력받은 문자열을 list(s)로 한 글자씩 분할
    3. 분할된 한글자 리스트를 순회하며
        - 1. idx = ord(c) - ord('a')
        - 2. alpha[idx] += 1
    # ===========================
    # Pass_02 : 문자열을 list(s)로 한글자씩 분할하지 않고 for i in range(len(s))를 이용해 s[i]로 활용
    #=========================================
    '''

    s = input()
    alpha = [0] * (ord('z') - ord('a') + 1)


    # c_list = list(s)
    #
    # for c in c_list:
    #     idx = ord(c) - ord('a')
    #     alpha[idx] += 1

    for i in range(len(s)):
        idx = ord(s[i]) - ord('a')
        alpha[idx] += 1


    print(f'#{tc} {" ".join(map(str,alpha))}')
