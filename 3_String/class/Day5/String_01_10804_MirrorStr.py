import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    '''
    1. origin과 mirror의 문자들을 인덱스를 일치시켜 선언
    2. 입력받은 문자열을 한글자씩 분할
    3. 분할된 문자열을 역순으로 정렬
    4. 역순 리스트를 순회하며
        - result.append(mirror[origin.index(ch)])
    '''

    origin = ['b', 'd', 'p', 'q']
    mirror = ['d', 'b', 'q', 'p']

    s = list(input())
    rev = s[::-1]
    result = []

    for ch in rev:
        result.append(mirror[origin.index(ch)])

    print(f'#{tc} {"".join(result)}')
