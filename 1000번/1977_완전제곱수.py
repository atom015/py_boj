"""
문제
M과 N이 주어질 때 M이상 N이하의 자연수 중 완전제곱수인 것을 모두 골라 그 합을 구하고 그 중 최솟값을 찾는 프로그램을 작성하시오. 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 완전제곱수는 64,  81,  100 이렇게 총 3개가 있으므로 그 합은 245가 되고 이 중 최솟값은 64가 된다.

입력
첫째 줄에 M이, 둘째 줄에 N이 주어진다. M과 N은 10000이하의 자연수이며 M은 N보다 같거나 작다.

출력
M이상 N이하의 자연수 중 완전제곱수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 단, M이상 N이하의 자연수 중 완전제곱수가 없을 경우는 첫째 줄에 -1을 출력한다.

예제 입력 1
60
100
예제 출력 1
245
64
예제 입력 2
75
80
예제 출력 2
-1

"""
from math import sqrt
def is_int(n):
    if int(n) == n: #정수인지검색
        return True #정수면 True
    return False #아니면 False를 return한다.
result = []
n = int(input())
m = int(input())
for i in range(n,m+1): #n부터 m+1까지 반복하면서
    if is_int(sqrt(i)) == True: #만약에 완전제곱수면
        result.append(i) #result에 추가해준다.
if len(result) == 0: #만약에 완전제곱수가 없으면
    print(-1) #-1출력
else: #만약에 완전제곱수가 있으면
    print(sum(result)) #더한값과
    print(min(result)) #제일 작은값출력
