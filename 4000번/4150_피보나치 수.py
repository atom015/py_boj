"""
문제
피보나치 수열은 다음과 같이 그 전 두 항의 합으로 계산되는 수열이다. 첫 두 항은 1로 정의된다.

f(1) = 1, f(2) = 1, f(n > 2) = f(n − 1) + f(n − 2)

정수를 입력받아, 그에 해당하는 피보나치 수를 출력하는 프로그램을 작성하여라.

예제 입력 1
100
예제 출력 1
354224848179261915075
힌트
해당 테스트 데이터의 모든 정답은 1000자를 넘지 않는다. ( f(20) = 6765 이므로 4자다. )
"""
import sys
sys.setrecursionlimit(50000)
n = int(input())
dp = [0 for i in range(n+1)]
dp[0] = 0
dp[1] = 1
def fibo(n):
    if n <= 1:
        return dp[n]
    else:
        if dp[n] > 0:
            return dp[n]
        else:
            dp[n] = fibo(n-1)+fibo(n-2)
            return dp[n]
print(fibo(n))
