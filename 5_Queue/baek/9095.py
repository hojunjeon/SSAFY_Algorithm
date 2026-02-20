t = int(input())

def ott_sum(n):
    if n == 0:
        return 1
    
    if n < 0:
        return 0
    
    return ott_sum(n-1) + ott_sum(n-2) + ott_sum(n-3)
    

for i in range(t):
    n = int(input())
    
    total = 0
    total = ott_sum(n)
    print(total)