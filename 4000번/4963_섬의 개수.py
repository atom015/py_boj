import sys
sys.setrecursionlimit(500000) #런타임에러가 나지않도록 재귀제한깊이를 늘려줬다.
#상하좌우 대각선까지 비교리스트
dx = [0,1,-1,0,1,-1,-1,1]
dy = [1,0,0,-1,1,1,-1,-1]
def dfs(x,y):
    chk[x][y] = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if li[nx][ny] == 1 and chk[nx][ny] == False:
                dfs(nx,ny)
while 1:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    li = [list(map(int,input().split())) for i in range(h)]
    chk = [[False for i in range(w)] for i in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if li[i][j] == 1 and chk[i][j] == False:
                cnt += 1
                dfs(i,j)
    print(cnt)
