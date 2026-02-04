import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    '''
    # 확인용 리스트 sudoku = [1, 2, 3, 4, 5, 6, 7, 8, 9] 선언
    # check_sudoku_linear() 함수 선언
    1. 행 우선 순회
        x : 0 - > 8 
        - arr[y][x] in sudoku 이면
            sudoku.remove(arr[y][x])
        - 아니면
            break
    # check_sudoku_box() 함수 선언
    1. 3x3 박스 순회하며 
        - arr[y][x] in sudoku 이면
            sudoku.remove(arr[y][x])
        - 아니면
            break

    '''
    arr = [list(map(int, input().split())) for _ in range(9)]

    def linear_check(arr):
        sudoku = [n for n in range(1, 10)]

        for y in range(9):
            check = sudoku[:]
            for x in range(9):
                if arr[y][x] in check:
                    check.remove(arr[y][x])
                else:
                    return 0
        return 1

    def box_check(arr):
        sudoku = [n for n in range(1, 10)]

        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                check = sudoku[:]
                for dy in range(3):
                    for dx in range(3):
                        if arr[y + dy][x + dx] in check:
                            check.remove(arr[y + dy][x + dx])
                        else:
                            return 0
        return 1

    trans = list(zip(*arr))

    result = []
    result = [linear_check(arr), linear_check(trans), box_check(arr)]

    if 0 in result:
        print(f'#{tc} {0}')

    else:
        print(f'#{tc} {1}')
