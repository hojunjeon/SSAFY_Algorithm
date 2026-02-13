def recursion(s, l, r):
    global cnt_r
    cnt_r += 1
    if l >= r: 
        return 1
    elif s[l] != s[r]: return 0
    else: 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    global cnt_p
    return recursion(s, 0, len(s)-1)

# print('ABBA:', isPalindrome('ABBA'))
# print('ABC:', isPalindrome('ABC'))

T = int(input())
for i in range(T):
    cnt_r = 0
    
    word = input()
    result = isPalindrome(word)
    print(result, cnt_r)