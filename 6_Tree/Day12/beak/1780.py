# 문제집공유용 5.재귀 1780 - 종이의 개수

cnt_1, cnt_0, cnt_m1 = 0, 0, 0

def is_all_one(arr):
    return all(all(x == 1 for x in row) for row in arr)
def is_all_zero(arr):
    return all(all(x == 0 for x in row) for row in arr)
def is_all_minus(arr):
    return all(all(x == -1 for x in row) for row in arr)

def paper(arr):
    global cnt_1
    global cnt_0
    global cnt_m1
    
    l = len(arr)
    
    if l == 1:
        if arr[0][0] == 1:
            cnt_1 += 1
        elif arr[0][0] == 0:
            cnt_0 += 1
        else:
            cnt_m1 += 1
        return
    
    if is_all_zero(arr):
        cnt_0 += 1
        return
    if is_all_one(arr):
        cnt_1 += 1
        return
    if is_all_minus(arr):
        cnt_m1 += 1
        return

    p1 = l // 3
    p2 = p1 * 2
    
    paper([row[:p1] for row in arr[:p1]])
    paper([row[p1:p2] for row in arr[:p1]])
    paper([row[p2:] for row in arr[:p1]])
    paper([row[:p1] for row in arr[p1:p2]])
    paper([row[p1:p2] for row in arr[p1:p2]])
    paper([row[p2:] for row in arr[p1:p2]])
    paper([row[:p1] for row in arr[p2:]])
    paper([row[p1:p2] for row in arr[p2:]])
    paper([row[p2:] for row in arr[p2:]])


    return
    
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

paper(arr)
print(cnt_m1)
print(cnt_0)
print(cnt_1)