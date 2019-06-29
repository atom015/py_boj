import sys
sys.setrecursionlimit(50000)  #재귀제한높이설정(이걸 기본값이상으로 안해주면 런타임에러가 난다.) ※기본값:1000
n,m = map(int,sys.stdin.readline().split()) #n:정점(node)의 개수,m:간선의 개수가주어진다.
#1부터시작하도록 n+1번 만들어준다
li = [[] for i in range(n+1)] #인접리스트를 만들어준다.
chk = [False for i in range(n+1)] #방문체크리스트
#입력
for i in range(m):
    u,v = map(int, sys.stdin.readline().split())
    li[u].append(v)
    li[v].append(u)

def dfs(nd):
    chk[nd] = True #방문체크
    for i in li[nd]: #현재노드에있는 값들을돈다(인접리스트는 연결되어 있는것만 들어있기 떄문에 1인지 체크안해주어도 된다.)
        if chk[i] is False: #만약에 방문한적이 없으면 재귀를돈다.
            dfs(i)
cnt = 0 #연결요소 개수체크
for i in range(1,n+1):
    if chk[i] is False: #만약에 chk[i]가 방문한적이없으면
        dfs(i) #함수에 i를넣고
        cnt += 1 #체크
print(cnt) #연결요소개수 출력
