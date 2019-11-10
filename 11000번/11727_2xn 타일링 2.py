n = int(input())
dp = [0 for i in range(n+1)]
dp[0],dp[1] = 1,1
for i in range(2,n+1):
    dp[i] = (dp[i-1]+dp[i-2]*2)%10007
print(dp[n])
# 2xn 타일 1과 푸는 방식이 같지만 앞에 두개의 타일로 만드는 경우가
# 2x2 박스로 만드는 경우가 추가되었기 때문에 Dp[i-2]에 2배를 곱해서 만들어가 바면 된다.
