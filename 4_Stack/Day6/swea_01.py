# [S/W 문제해결 기본] 10일차 - 비밀번호
import sys
sys.stdin = open('SSAFY_Algorithm\\4_Stack\Day6\input.txt','r')

T = int(input())

for tc in range(1, T + 1):
    num = int(input())
    cnt = 0

    # =======================
    # 1. 반복문 구현

    # while True:
    #     if num == 1:
    #         break

    #     if num % 2 == 0 :
    #         num //= 2
    #     else :
    #         num = num * 3 + 1

    #     cnt += 1

    # =======================

    # =======================
    # 2. 재귀함수 구현
    def collatz(num) :
        if num == 1:
            return 0
        
        if num % 2 == 0:
            return 1 + collatz(num // 2)
        else :
            return 1 + collatz(num * 3 + 1)
        
    cnt = collatz(num)
    # =======================

    
    print(f'#{tc} {cnt}')