import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1, T + 1 ):

    n_list = list(map(int, input().split()))

    n = n_list[0]
    n_list.pop(0)

    avg = sum(n_list) / n
    over_avg = 0

    for score in n_list:
        if score > avg :
            over_avg += 1

    pct = (over_avg / n) * 100

    print(f'{pct:.3f}%')