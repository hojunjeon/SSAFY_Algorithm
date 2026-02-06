import sys
sys.stdin = open('input.txt', 'r')

# T = int(input())

# for tc in range(1, T + 1):
n, x = map(int,input().split())

arr = list(map(int, input().split()))

window = sum(arr[:x])
max_visit = window
count = 1

for i in range(n - x):
    window = window - arr[i] + arr[x + i]
    if max_visit == window :
        count += 1

    if max_visit < window :
        count = 1
        max_visit = window
    

if max_visit == 0:
    print('SAD')
else :
    print(max_visit)
    print(count)