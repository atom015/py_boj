import sys
sys.setrecursionlimit(100000)
ip = sys.stdin.readline
def is_palindrome(s):
    return s == s[::-1]
def can_palindrome(l,r,chk):
    if l > r:
        return True
    if s[l] == s[r]:
        return can_palindrome(l+1,r-1,chk)
    elif chk:
        return any([can_palindrome(l+1,r,False),can_palindrome(l,r-1,False)])
    else:
        return False
def func(s):
    if is_palindrome(s):
        return 0
    elif can_palindrome(0,len(s)-1,1):
        return 1
    else:
        return 2

for i in range(int(ip())):
    s = ip().strip()
    print(func(s))
