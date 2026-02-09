max_len = 0
arr = [list(input()) for _ in range(5)]
max_len = max(len(row) for row in arr)

for y in range(5):
    for _ in range(max_len - len(arr[y])):
        arr[y].append('@')

result = []
for x in range(max_len):
    for y in range(5):
        if arr[y][x] == '@':
            continue
        result.append(arr[y][x])

print("".join(result))
