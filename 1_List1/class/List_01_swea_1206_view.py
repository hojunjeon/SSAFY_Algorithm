for tc in range(10):

    T = int(input())
    apt = list(map(int, input().split()))
    view = 0

    for i in range(2, T-2):

        # if max(apt[j] for j in range(i-2, i+3)) == apt[i]:
        #     view += apt[i] - max(apt[j] for j in range(i-2, i+3) if j != i)

        first = 0  # 5개 건물 중 가장 높은 층
        second = 0  # 두번째로 높은 층

        for j in range(i-2, i+3):  # 중간 건물 기준 왼쪽 2개, 오른쪽 2개 비교

            if first < apt[j]:  # 가장 큰 건물을 first에
                second = first
                first = apt[j]

            elif second < apt[j]:   #두번째로 크다면 second에
                second = apt[j]

        if first == apt[i]:     # 만약 기준 건물이 인근 건물 중 가장 크다면
            view += first - second  # 차이를 view에 저장

        # print(view)

    print(f'#{tc + 1} {view}')