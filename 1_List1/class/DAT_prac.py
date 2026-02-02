T = int(input())

# 테스트케이스를 반복
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]

    count_dat = [0] * 10000001  # 올 수 있는 모든 사원번호

    # 이차원 리스트 값 직접 접근
    # for row in matrix:
    #     for num in row:
    #         pass

    # 이차원 리스트 인덱스 접근
    for i in range(H):
        for j in range(W):
            target = matrix[i][j]
            count_dat[target] += 1

    # 내장 함수 사용 시
    # max_count = max(count_dat)  # 최대값
    # max_index = count_dat.index(max_count)  # 최대값의 위치(인덱스)

    # Todo : max, index 쓰지 않고 구현한다면 ?

    max_count = 0
    max_index = 0
    for i in range(len(count_dat)):
        if max_count < count_dat[i]:
            max_count = count_dat[i]
            max_index = i
    print(f"#{tc} {max_index}")