c,k = map(int,input().split())
tmp = 10**k
ans = c // tmp*tmp
if c % tmp >= tmp//2: #만약에 반올림을 해야하면
    ans += tmp #k번째의값에 +1해준다.
print(ans)
