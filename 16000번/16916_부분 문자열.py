def Gp(p):
    m = len(p)
    pi = [0 for i in range(m)]
    j = 0
    for i in range(1,m):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j += 1
            pi[i] += j
    return pi
def kmp(s,p):
    ans = []
    pi = Gp(p)
    n,m,j = len(s),len(p),0
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = pi[j-1]
        if s[i] == p[j]:
            if j == m-1:
                ans.append(i-m+2)
                j = pi[j]
            else:

                j += 1
    return ans
s = input()
p = input()
ans = kmp(s,p)
print(1 if len(ans) else 0)
