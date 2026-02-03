pay = 1000
coin = [500, 100, 50, 10, 5, 1]
arr = []

price = int(input())
change = pay - price

for c in coin:
    count = change // c
    arr.append(count)
    change -= count * c

print(sum(arr))