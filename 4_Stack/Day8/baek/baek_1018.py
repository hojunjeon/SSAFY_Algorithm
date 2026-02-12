# 입문 1018 체스판 다시 칠하기

# import sys
# sys.stdin = open('input.txt','r')

# T = int(input())

# for tc in range(1, T+ 1):

n, m = map(int, input().split())

board = [input() for _ in range(n)]
k = 8

SB = ["BWBWBWBW","WBWBWBWB"] * 4
SW = ["WBWBWBWB","BWBWBWBW"] * 4

min_cnt = k**2 // 2 + 1
for sy in range(n - k + 1):
    for sx in range(m - k + 1):
        check_b = SB
        check_w = SW
        cnt_b = 0
        cnt_w = 0
        for dy in range(k):
            for dx in range(k):
                if board[sy + dy][sx + dx] != check_b[dy][dx]:
                    cnt_b += 1
                if board[sy + dy][sx + dx] != check_w[dy][dx]:
                    cnt_w += 1
                
        if min_cnt > cnt_b:
            min_cnt = cnt_b
        if min_cnt > cnt_w:
            min_cnt = cnt_w
        
print(f"{min_cnt}")
