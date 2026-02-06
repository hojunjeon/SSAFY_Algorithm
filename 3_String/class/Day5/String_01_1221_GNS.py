import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    '''
    1. i : 0 -> 9 순회하며 
        - 1. cnt[i] = str_list.count(str2int[i])
    2. i : 0 -> 9 
        - 1. print(str2int[i] * cnt[i])     
    '''
    case, n = input().split()

    str_list = list(input().split())
    str2int = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    cnt = [0] * 10

    for i in range(10):
        cnt[i] = str_list.count(str2int[i])

    print(f"#{tc}")
    for i in range(10):
        print(f'{str2int[i]} ' * cnt[i])
