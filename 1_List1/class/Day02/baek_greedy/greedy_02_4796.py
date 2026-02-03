i = 1
while True:
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0:
        break

    using_day = 0
    count = V // P

    using_day = count * L
    left_day = V - count * P

    if left_day > L:
        using_day += L
    else:
        using_day += left_day
    print(f'Case {i}: {using_day}')

    i += 1
