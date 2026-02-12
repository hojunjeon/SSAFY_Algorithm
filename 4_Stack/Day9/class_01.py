# # =============================
# # 전체 경우의 수 (기본 재귀 호출)

# # 주사위 K개의 조합

# # 시작 : 주사위 하나도 안던짐
# # 끝 : 주사위 K개를 던짐
# # prameter :
# #   - cnt : 던진 횟수
# #   - path : 던진 주사위 기록

# K = 3
# def dice(cnt, path):

#     if cnt == K:
#         print(path)
#         return
    
#     for i in range(1, 7):
#         path.append(i)
#         dice(cnt + 1, path)
#         path.pop()

#     # path.append(1)
#     # dice(cnt + 1, path) # [1,1,1] 만들고

#     # path.pop()  # path의 마지막 을 없애고 이제 2를 push
#     # path.append(2)
#     # dice(cnt + 1, path)

#     # path.pop()  # path의 마지막 을 없애고 이제 3를 push
#     # path.append(3)
#     # dice(cnt + 1, path)

# path = dice(0, [])



# # ========================================================
# # 부분 집합

# # 시작 : 0개의 데이터를 부분집합에 넣을 지 말지 고려
# # 끝 : 모든 데이터를 부분집합에 넣을지 말지 고려
# # 누적값
# #   cnt : 몇개의 데이터를 고려했는가
# #   subset: 현재 부분집합
# arr = [ "A", "B", "C"]

# def recur2(idx, subset):

#     if  idx == len(arr):
#         print(subset)
#         return
    
#     # 1. 현재 원소를 부분집합에 포함 O
#     subset.append(arr[idx])
#     recur2(idx + 1, subset)
#     subset.pop()

#     #2. 현재 원소를 부분집합에 포함 X
#     recur2(idx + 1, subset)

# recur2(0,[])



# # ============================
# # 3. 중복 순열 Permutation with repetition 
# # - A B C D 중복 허용하여 3개를 뽑는 경우

# arr = ["A","B","C","D"]

# def recur3(cnt, pr):

#     if cnt == 3:
#         print(pr)
#         return
    
#     for i in range(len(arr)):
#         pr.append(arr[i])
#         recur3(cnt + 1, pr)
#         pr.pop()

# recur3(0,[])



# # ==============================
# # 4. 순열
# # - A B C D 중복 허용하지 않고 3개를 뽑는 경우
# # - 중복 순열에서 중복을 제거하는 부분만 추가

# arr = ["A","B","C","D"]
# used = [0] * len(arr)

# def recur4(cnt, permuteation):
    
#     if cnt == 3:
#         print(permuteation)
#         return

#     for i in range(len(arr)):
#         # 이미 arr[i]가 포함되어 있다면
#         if used[i]:
#             # 포함하지 않음
#             continue
#         # 리스트에 append 하고 사용됨을 나타내기 위해 used[i] = 1
#         # return 이후 pop 하면 사용하지 않음을 나타내기 위해 used[i] = 0
#         permuteation.append(arr[i])
#         used[i] = 1
#         recur4(cnt + 1, permuteation)
#         permuteation.pop()
#         used[i] = 0
        
# recur4(0,[])



# =============================
# 5. 조합
# - A B C D 중복 허용하지 않고 순서를 고려하지 않고 3개를 뽑는 경우
# - 
arr = ["A","B","C","D"]
K = 3

# 기본형
def recur5(cnt, path):
    if len(path) == K:
        print(path)
        return
    
    for i in range(cnt, len(arr)):
        path.append(arr[i])
        recur5(i + 1, path)
        path.pop()
        
recur5(0, [])

# 이전에 입력한 요소를 입력
# def recur5(cnt, pre, path):
#     if cnt == K:
#         print(path)
#         return
    
#     for i in range(pre + 1, len(arr)):
#         path.append(arr[i])
#         recur5(cnt + 1, i, path)
#         path.pop()

# recur5(0, -1, [])