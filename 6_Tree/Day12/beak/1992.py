# 문제집공유용 5.재귀 1992 - 쿼드트리

n = int(input())

video = [list(input()) for _ in range(n)]

def is_all_one(arr):
    return all(all(x == '1' for x in row) for row in arr)
def is_all_zero(arr):
    return all(all(x == '0' for x in row) for row in arr)

ans = []
def quad_tree(arr):

    result = ["("]
    if is_all_one(arr):
        return "1"
    elif is_all_zero(arr):
        return "0"

    y_mid = len(arr) // 2
    x_mid = len(arr[0]) // 2
    
    arr_ul = [row[:x_mid] for row in arr[:y_mid]]
    arr_ur = [row[x_mid:] for row in arr[:y_mid]]
    arr_dl = [row[:x_mid] for row in arr[y_mid:]]
    arr_dr = [row[x_mid:] for row in arr[y_mid:]]
    
    result.extend(quad_tree(arr_ul))
    result.extend(quad_tree(arr_ur))
    result.extend(quad_tree(arr_dl))
    result.extend(quad_tree(arr_dr))
    result.extend(")")
    
    return result

ans = quad_tree(video)
print(''.join(ans))
