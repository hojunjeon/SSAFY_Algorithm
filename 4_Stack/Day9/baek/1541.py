# 문제집공유용 2.greedy 잃어버린 괄호

import sys
sys.stdin = open('input.txt', 'r')

'''
1. '-'를 기준으로 문자열 분리
2. 분리된 문자열 묶음 계산
    - 문자열에 '+'가 포함 되어 있다면
        - '+'를 기준으로 문자열을 분리하고 / 정수형태로 변환 후 모두 sum
    - sum 한 값을 result에서 빼줌
'''
s = input()
lst = list(s.split('-'))

result = None
for i in range(len(lst)):
    temp = lst[i]
    if '+' in lst[i]:
        temp = map(int,lst[i].split('+'))
        temp = sum(temp)
        
    if result == None:
        result = int(temp)
    else:
        result -= int(temp)
        
print(result)
    