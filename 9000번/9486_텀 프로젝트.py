import sys
ip = sys.stdin.readline
def dfs(start,nd,cnt):
    if v[nd]:
        #첫번째로 dfs를 시작한 학생이 맞는지 체크
        if fir[nd] != start:
            return 0
        # 사이클 해당되는 학생수
        return cnt - v[nd]

    fir[nd] = start # 시작노드를 넣어준다.
    v[nd] =  cnt #현재노드에 cnt를 넣어준다.
    return dfs(start,arr[nd],cnt+1)
for i in range(int(ip())):
    n = int(ip())
    ans = 0
    arr = [0]+list(map(int,ip().split()))
    fir = [0 for i in range(n+1)] #첫번째로 dfs시작한 학생번호
    v = [0 for i in range(n+1)] # 방문체크
    for i in range(1,n+1):
        if not v[i]:
            ans += dfs(i,i,1)
    print(n-ans)
#참고: https://lmcoa15.tistory.com/51
