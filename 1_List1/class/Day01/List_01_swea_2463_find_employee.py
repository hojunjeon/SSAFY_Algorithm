T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())

    emp_list = []
    emp_dict = {}

    for i in range(H):
        emp_list = list(map(int, input().split()))

        for emp in emp_list:
            emp_dict[emp] = emp_dict.get(emp, 0) + 1

    max_val = max(emp_dict.values())

    max_keys = [k for k, v in emp_dict.items() if v == max_val]

    print(f'#{tc} {min(max_keys)}')
