MAX = 10000
a = [False for i in range(MAX+1)]
for i in range(2,MAX+1):
    if not a[i]:
        for j in range(i*i,MAX+1,i):
            a[j] = True
for i in range(int(input())):
    n = int(input())
    ans = {}
    for i in range(2,MAX+1):
        if i > n:
            break
        if a[i] is False:
            j = n-i
            if a[j] is False:
                ans[abs(i-j)] = [i,j]
    ret = [1e9,0]
    for k,v in ans.items():
        if k < ret[0]:
            ret[0] = k
            ret[1] = v
    print(min(ret[1][0],ret[1][1]),max(ret[1][0],ret[1][1]))
