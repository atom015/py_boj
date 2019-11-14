n = int(input())
ret = list(input())
for i in range(n-1):
    s = input()
    for i in range(len(s)):
        if ret[i] != s[i]:
            ret[i] = "?"
print("".join(ret))