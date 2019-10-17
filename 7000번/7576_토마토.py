import sys,collections
ip = sys.stdin.readline
n,m = map(int,ip().split())
arr = [list(map(int,ip().split())) for i in range(m)]
dx = [0,1,-1,0]
dy = [1,0,0,-1]
q = collections.deque([])
#시작위치 q에 넣기
def snd():
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                q.append([i,j,0])
                arr[i][j] = 1
snd()
#-1출력할지 말지 결정코드
def chk(a,n,m):
    for i in range(m):
        if 0 in a[i]:
            return False
#bfs 탐색
while len(q) != 0:
    x,y,day = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if arr[nx][ny] == 0:
                q.append([nx,ny,day+1])
                arr[nx][ny] = 1
if chk(arr,n,m) == False:
    print(-1)
else:
    print(day)
