N = int(input())
dp = [[0 for i in range(N+1)] for i in range(N+1)]
arr = [0]+list(map(int,input().split()))

# 자기자신 즉, 한글자는 무조건 팰린드롬이라는 것이다.
for i in range(1,N+1):
    dp[i][i] = 1

# 현재 값과 앞에 있는값이 같으면 팰린드롬이다.(예시:aa,bb)
for i in range(1,N):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

# k칸 다음번째
for k in range(2,N):
    # 1 ~ (n-k)번째 까지
    for i in range(1,N-k+1):
        j = i+k
        if arr[i] == arr[j] and dp[i+1][j-1]:
            dp[i][j] = 1

for i in range(int(input())):
    a,b = map(int,input().split())
    print(1 if dp[a][b] else 0)
