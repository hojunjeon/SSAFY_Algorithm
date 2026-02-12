# 문제집공유용 3.슬라이딩윈도우 10025 게으른 백곰
n, k = map(int,input().split())
temp = [list(map(int, input().split())) for _ in range(n)]

end = max(temp, key = lambda x:x[1])[1]
lst = [0] * (end+1)

for g, x in temp:
    lst[x] = g
    
window = sum(lst[0:k*2+1])
max_w = window


for start in range(1, end - k*2 + 1):
    window = window - lst[start - 1] + lst[start + k*2]
    if max_w < window:
        max_w = window
        
print(max_w)

