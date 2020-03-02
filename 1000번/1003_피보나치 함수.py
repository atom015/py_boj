#일반 메모이제이션 방식으로 피보나치를 구한함수이다.
def fibo(n):
    if n == 0:
        dp[n] = 0
        return dp[n]
    if n == 1:
        dp[n] = 1
        return dp[n]
    else:
        if dp[n] > 0:
            return dp[n]
        else:
            dp[n] = fibo(n-1) + fibo(n-2)
            return dp[n]

for i in range(int(input())):
    n = int(input())
    #n이 0이면 1 0출력 n이 1이면 0 1출력(이게 기본 출력이다.)
    if n == 0:
        print("1 0")
        continue
    if n == 1:
        print("0 1")
        continue
    dp = [0 for i in range(n+1)]
    fibo(n)
    print(dp[n-1],dp[n]) #0의개수 : fibo(n-1),1의개수 : fibo(n)
