"""
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1≤M≤100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수들의 범위는 int 로 한다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

예제 입력 1
5
4 1 5 2 3
5
1 3 7 9 5
예제 출력 1
1
1
0
0
1
"""
n = int(input())
nl = sorted(list(map(int,input().split())))
m = int(input())
ml = list(map(int,input().split()))
#이진검색으로 해주면된다.
def binary_search(n,lo,hi,li):
    if lo > hi:
        return 0
    mid = (lo+hi) // 2
    if li[mid] == n:
        return 1
    if li[mid] < n:
        lo = mid + 1
    else:
        hi = mid - 1
    return binary_search(n,lo,hi,li)
for i in ml:
    print(binary_search(i,0,n-1,nl))
