n,k = map(int,input().split())
arr = [0 for i in range(n+1)]
for i in range(n):
    a,b,c,d= map(int,input().split())
    arr[a] = b*(10**12)+c*(10**6)+d
rank = 1
for i in range(1,n+1):
    if arr[i] > arr[k]: #자기보다 점수가큰것은 자기보다 점수가높은것이므로 등수를 +1해준다.
        rank += 1
print(rank)
#금은동을 점수화했다.
#금:10**12점
#은:10**6점
#동:1점
