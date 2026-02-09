import sys
sys.stdin = open('input.txt','r')

count = set()

lst = [int(input()) for _ in range(10)]

for num in lst:
    r = num % 42

    count.add(r)

print(len(count))


