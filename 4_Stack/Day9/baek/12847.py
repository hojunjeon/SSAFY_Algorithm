# 문제집공유용 3.슬라이딩윈도우 12847 꿀아르바이트

n, m = map(int, input().split())

pay = list(map(int, input().split()))

window = sum(pay[0:m])
max_pay = window

for start in range(1, len(pay) - m + 1):
    end = start + m -1
    window = window - pay[start-1] + pay[end]
    if max_pay < window:
        max_pay = window
        
print(max_pay)