T = int(input())

for tc in range(1, T + 1):

    # 아파트 주민
    h1, w2 = map(int, input().split())
    apt = []
    for _ in range(h1):
        f1 = list(map(int, input().split()))
        apt.extend(f1)

    # 블랙리스트
    h2, w2 = map(int, input().split())
    black = set()
    for _ in range(h2):
        f2 = list(map(int, input().split()))
        black.update(f2)

    black_list = []
    citizen_list = []

    for p in apt:
        if p in black:
            black_list.append(p)
        else:
            citizen_list.append(p)

    print(f'#{tc} {len(black_list)} {len(citizen_list)}')

