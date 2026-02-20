# 문제집공유용 5.재귀 2630 - 색종이 만들기
# import sys
# lines = sys.stdin.readlines()

cnt_white, cnt_blue = 0, 0

def is_all_one(arr):
    return all(all(x == 1 for x in row) for row in arr)
def is_all_zero(arr):
    return all(all(x == 0 for x in row) for row in arr)

def color(arr):
    global cnt_blue
    global cnt_white
    
    l = len(arr)
    
    if l == 1:
        if arr[0][0] == 1:
            cnt_blue += 1
        else:
            cnt_white += 1
        return
    
    if is_all_zero(arr):
        cnt_white += 1
        return
    if is_all_one(arr):
        cnt_blue += 1
        return

    mid = l // 2
    
    color([row[:mid] for row in arr[:mid]])
    color([row[:mid] for row in arr[mid:]])
    color([row[mid:] for row in arr[:mid]])
    color([row[mid:] for row in arr[mid:]])

    return
    
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

color(arr)
print(cnt_white)
print(cnt_blue)