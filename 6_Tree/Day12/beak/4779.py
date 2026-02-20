# 문제집공유용 5.재귀 4779 - 칸토어 집합
import sys
lines = sys.stdin.readlines()

def cantor(arr):
    
    length = len(arr)
    if length == 1:
        return arr
    p1 = length // 3
    p2 = p1 * 2
    
    for i in range(p1, p2):
        arr[i] = " "
    
    a1 = cantor(arr[:p1])
    a2 = arr[p1:p2]
    a3 = cantor(arr[p2:])
    
    return a1+a2+a3
    

for line in lines:
        n = int(line.strip())
        arr = ['-'] * (3 ** n)
        
        result = cantor(arr)
        print(''.join(result))