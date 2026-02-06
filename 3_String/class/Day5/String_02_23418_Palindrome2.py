import sys

sys.stdin = open('input.txt', 'r')
'''
# =====================
# def palindrome(txt) 함수 선언
1. i : 0 -> len(txt) // 2 -1
    - 1. txt[i] != txt[len(txt) - 1 - i] 이면 return 0;
    - 2. 아니면 return len(txt)
# ===================
# def find_max_palindrome(arr) 함수
1. 문자열이 저장된 배열을 입력받아 한줄 씩 순회
2. 2중 반복문 start : 0 -> 99
    end : 100 -> start + 1 
    - 1. palindrome(arr[i:j]) 실행
    - 2. return 값과 max_len을 비교해 return이 크다면 max_len 교체
# ======================
# 본문 
1. 문자열을 입력 받아 배열로 저장하고 find_max_palindrome(arr) 실행
2. arr을 전치시켜 다시 한번 find_max_palindrome(trans_arr) 실행
3. 1, 2번의 결과 값을 비교해 더 큰값을 max_length에 저장 후 print
'''


def palindrome(txt):
    word_len = len(txt)
    for i in range(word_len // 2):
        if txt[i] != txt[word_len - 1 - i]:
            return False
    return True


def find_max_palindrome(arr):
    for k in range(100, 0, -1):
        for s in range(100):
            for i in range(100 - k + 1):
                temp = arr[s][i: i + k]
                flag = palindrome(temp)
                if flag:
                    return k


T = 10

for tc in range(1, T + 1):
    case = input()
    y = 100
    x = 100

    arr = [input() for _ in range(y)]
    trans = list(zip(*arr))
    max_len = find_max_palindrome(arr) if find_max_palindrome(arr) > find_max_palindrome(trans) else find_max_palindrome(trans)

    print(f'#{tc} {max_len}')
