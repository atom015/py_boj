n,m = map(int,input().split())
arr = list(map(int,input().split()))
end = 0
Sum = 0
ans = 0
for start in range(n):
    while end < n and Sum < m:
        Sum += arr[end]
        end += 1
    if Sum == m:
        ans += 1
    Sum -= arr[start]
print(ans)
