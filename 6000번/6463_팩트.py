"""
문제
N!은 "N 팩토리얼"로 읽으며, 처음 N개의 양의 정수를 곱한 값이다. 이때, N은 음이 아닌 정수이어야 한다. 예를 들면 다음과 같다.

 N       N!
 0       1
 1       1
 2       2
 3       6
 4      24
 5     120
10 3628800
N을 입력 받아 0이 아닌 마지막 자리를 구하는 프로그램을 작성하시오. 예를 들어, 5!의 경우에 정답은 2이다. 5! = 120이고, 2는 0이 아닌 마지막 자리이기 때문이다.

입력
입력은 10000을 넘지 않는 음이 아닌 정수로 이루어져 있으며, 한 줄에 하나씩 주어진다. 각각의 정수는 N이며, 이를 입력받아 N!의 0이 아닌 마지막 자리를 출력해야 한다.

출력
입력으로 주어진 각각의 N에 대해서, 1~5열에는 N을 오른쪽 정렬로 출력하고, 6~9열에는 " -> ", 10열에는 N!의 0이 아닌 마지막 자리를 출력한다.

예제 입력 1
1
2
26
125
3125
9999
예제 출력 1
    1 -> 1
    2 -> 2
   26 -> 4
  125 -> 8
 3125 -> 2
 9999 -> 8
"""
from math import factorial
compare = 0
result = {}
while 1:
    try:
        n = int(input())
        if compare < len(str(n)):
            compare = len(str(n))
        li = list(str(factorial(n)))[::-1]
        for i in li:
            if "0" != i:
                ans = i
                break
        result["{} -> {}".format(n,ans)] = len(str(n))
    except :
        break

for k,v in result.items():
    print(" "*(compare-v)+"",k)
