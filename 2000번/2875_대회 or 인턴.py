n,m,k = map(int,input().split())
cnt = 0
while n >= 2 and m >= 1 and n+m >= 3+k:
    n -= 2
    m -= 1
    cnt += 1
print(cnt)
#n은 2보다 커야하고 m은 1보다커야한다는 조건은 대회에는 2명과 1명이 나가야하기때문이다.
#그리고 마지막에 n+m이 3+k보다 커야하는조건은 k명이 반드시 참가하야하는 것때문이다.
