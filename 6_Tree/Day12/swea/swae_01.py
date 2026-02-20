# swea Tree2 [S/W 문제해결 기본] 9일차 - 사칙연산

import sys
sys.stdin = open("02_SSAFY_Algorithm\\6_Tree\Day12\swea\input.txt","r")

def post(tree, root):
    if root == -1:
        return 0
    left = tree[root][1]   
    right = tree[root][2]
    l = post(tree, left)
    r = post(tree, right)
    if str(tree[root][0]).isdigit():
        return tree[root][0]
    if tree[root][0] == "+":
        return l + r
    if tree[root][0] == "-":
        return l - r
    if tree[root][0] == "*":
        return l * r
    if tree[root][0] == "/":
        return int(l / r)
T = 10
for tc in range(1, T + 1):
    tree = [0]
    n = int(input())
    for _ in range(n):
        temp = input().split()
        if temp[1].isdigit():
            tree.append([int(temp[1]), -1, -1])
        else:
            tree.append([temp[1], int(temp[2]), int(temp[3])])
    ans = post(tree, 1)
    print(f'#{tc} {ans}')