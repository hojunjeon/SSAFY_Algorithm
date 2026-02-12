# 문제집공유용 2.greedy 1931 회의실 배정

import sys
sys.stdin = open('input.txt','r')

'''
입력받은 회의시간을 끝나는 시간 기준으로 정렬
회의시간이 빨리 끝나는 회의 먼저 회의실 배정
+
끝나는 시간이 같다면 시작 시간이 빠른 순으로 정렬
'''

n = int(input())
time = []

for _ in range(n):
    time.append(list(map(int, input().split())))

table = sorted(time, key = lambda x: (x[1],x[0]))
cnt = 0
end = 0

for s,e in table:
    
    if s >= end:
        cnt += 1
        end = e
    
print(cnt)