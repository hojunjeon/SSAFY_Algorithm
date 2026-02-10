# 입문 1018 체스판 다시 칠하기

from pprint import pprint

import sys
sys.stdin = open('SSAFY_Algorithm\\0_IM\\01_start\input.txt','r')

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

pprint(board)

P = board[0][0]
color = ['W', 'B']
if P == 'W':
    start = 0
else:
    start = 1

k = 8
for start_y in range(n - k + 1):
    for start_x in range(n - k + 1):
        board[start_y][start_x]
