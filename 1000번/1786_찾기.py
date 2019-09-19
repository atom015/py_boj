# KMP algorithm:
# 문자열 S에서 W 찾기 ! -> O(N+M) (N = len(S), M = len(W))
# KMP에는 실패 함수가 존재한다. -> 불일치가 발생했을 때 얼마나 건너뛸 것인지?
# fail(x) = W의 처음 (x+1)글자 중, 일치하는 접두/접미사 중 최대 길이
def mk(n):
    n_size = len(n)
    table = [0 for i in range(n_size)]
    j = 1
    i = 0
    while j + i < n_size:
        if n[i] == n[j+i]:
            i += 1
            table[j+i-1] = i
        else:
            if i == 0:
                j += 1
            else:
                j += i - table[i-1]
                i = table[i-1]
    return table
def kmp(s,p):
    ans = []
    table = mk(p)
    n,m,j = len(s),len(p),0
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = table[j-1]
        if s[i] == p[j]:
            if j == m-1:
                ans.append(i-m+2)
                j = table[j]
            else:
                j += 1
    return ans
s = input()
p = input()
ans = kmp(s,p)
print(len(ans))
for i in ans:
    print(i)
