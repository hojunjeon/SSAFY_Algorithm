import sys

sys.stdin = open('input.txt', 'r')

case_num = int(input())
arr = [list(map(int, input().split())) for _ in range(100)]

print(arr[:][0])