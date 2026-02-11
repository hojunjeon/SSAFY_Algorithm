# 백트래킹 기초


# 백트래킹이란 ?
# - 재귀 함수에서 적합하지 않는 후보 해들을 확인하지 않고 되돌아가서 다른 후보 해들을 찾는 기법

# def backtracking():
#     if 기저 조건:
#         return
#
#     if 유망하지않다면:
#         return
#
#     for 가능한 모든 선택지를 확인:
#         if 유망하지않다면:
#             continue
#
#         현재 선택지를 해에 추가
#         다음 재귀호출
#         선택지를 해에서 제거 (백트랙)



# 예제: 숫자 리스트에서 숫자 조합을 뽑아 합이 K 가 되도록 하는 조합 모두 구하기
numbers = [7, 2, 3, 6]
K = 7
result = []


# 시작점: 누적합(0)
# 종료지점: 누적합이 K 이상
def backtracking(current_sum, path):
    if current_sum == K:  # 이미 K 라면, 더 이상 고를 필요가 없다.
        result.append(path[:])  # 결과 저장
        return

    if current_sum > K:  # 이미 K 보다 크다면 더 이상 고를 필요가 없다.
        return

    for i in range(len(numbers)):
        path.append(numbers[i])  # 숫자 하나를 선택
        backtracking(current_sum + numbers[i], path)  # 고른 숫자만큼 더 해준다.
        path.pop()               # 숫자 선택을 제거


backtracking(0, [])
print(result)