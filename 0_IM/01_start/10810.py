import sys
sys.stdin = open('input.txt','r')

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]

boxes = [0] * (n + 1)

for row in arr:
    start = row[0]
    end = row[1] + 1
    ball = row[2]

    for i in range(start, end):
        boxes[i] = ball

print(*boxes[1:])
