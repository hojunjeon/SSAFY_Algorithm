# 재귀 함수

arr = [5, 2, 3, 4, 1]

def recur(arr, i):

    if i == len(arr):
        return
    else :
        print(arr[i])
        recur(arr, i + 1)



def recur2(arr, i):

    if i == len(arr):
        return
    else :
        recur2(arr, i + 1)
        print(arr[i])


recur2(arr, 0)
recur(arr, 0)


