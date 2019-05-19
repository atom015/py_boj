N = int(input())
i = 0
ans = 0
while 1:
    if i == N+1:break
    
    if i == 1:ans+=5
    else:ans += 3 * (i-1) + 4
    
    ans %= 45678
    i += 1
print(ans-1)