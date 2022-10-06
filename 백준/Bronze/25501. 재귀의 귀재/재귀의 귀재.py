def recursion(s, l, r):
    if l >= r: return [1,l]
    elif s[l] != s[r]: return [0,l]
    else: return recursion(s, l+1, r-1)

def isPalindrome(s,cnt):
    return recursion(s, cnt, len(s)-1)


N = int(input())

for i in range(N):
    s = input()
    cnt = 0
    print(isPalindrome(s,cnt)[0],isPalindrome(s,cnt)[1]+1)

