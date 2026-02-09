import sys
sys.stdin = open('input.txt','r')

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

result = [[0] * m for _ in range(n)]

for y in range(n):
    for x in range(m):
        result[y][x] = a[y][x] + b[y][x]

for y in range(n):
    print(*result[y])