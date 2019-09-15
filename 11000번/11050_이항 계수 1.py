"""
문제
자연수N 과 정수K 가 주어졌을 때 이항 계수(N/K) 를 구하는 프로그램을 작성하시오.

입력
첫째 줄에N과K가 주어진다. (1 ≤ N ≤ 10, 0 ≤ K ≤ N)

출력
(N/K) 를 출력한다.

예제 입력 1
5 2
예제 출력 1
10
"""
n,k = map(int,input().split())
def Fact(n):
    mul = 1
    for i in range(1,n+1):
        mul *= i
    return mul
print(int(Fact(n) / (Fact(k)*Fact(n-k))))
