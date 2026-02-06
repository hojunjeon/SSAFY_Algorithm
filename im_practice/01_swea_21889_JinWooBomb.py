import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    '''
    # 지도 input() 단계에서 폭탄(@)의 좌표를 coordinates 리스트에 저장
    1. 지도에서 폭탄 좌표에 접근 -> 폭발상태(%) 로 변경
    2. 폭탄 좌표에서 delta를 순회하며 한 방향 씩 접근
        - 1. delta * di (di : 1 -> k)
            # 범위 지정
            - 1 ) 벽(#) 일 경우 
                continue
            - 2 ) 나머지 폭발상태(%)로 변환
             
    '''

    y, x = map(int, input().split())
    k = int(input())

    # bomb = [list(map(int, input().split())) for _ in range(y)]
    bomb = []
    coordinates = []

    # 입력과 동시에 @를 찾아 좌표 저장
    for dy in range(y):
        bomb.append(list(input()))
        coordinates.extend([[dy, i] for i, x in enumerate(bomb[dy]) if x == '@'])

    delta = [[-1,0], [1, 0], [0,-1], [0, 1]]

    for coordinate in coordinates:
        bomb[coordinate[0]][coordinate[1]] = '%'
        for d in delta:
            for di in range(1, k+1):

                # 범위 지정
                # coor[0] + d[0] * di
                # 최소 : 0 / 최대 : y -1
                if coordinate[0] + d[0] * di < 0 or coordinate[0] + d[0] * di > y - 1:
                    continue
                # coor[1] + d[1]*di
                # 최소 : 0 / 최대 : x -1
                if coordinate[1] + d[1] * di < 0 or coordinate[1] + d[1] * di > x - 1:
                    continue

                # 벽(#)이라면 다음 delta로 (di가 k까지 가지 않더라도 벽에 막힌 순간 나아갈 수 없기 때문)
                if bomb[coordinate[0] + d[0] * di][coordinate[1] + d[1] * di] == '#':
                    break

                bomb[coordinate[0] + d[0] * di][coordinate[1] + d[1] * di] = '%'

    print(f"#{tc}")
    for row in bomb:
        print(''.join(row))

