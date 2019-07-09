import sys,copy
sys.setrecursionlimit(500000)
n = int(input())
dx = [1,0,-1,0]
dy = [0,-1,0,1]
li = [list(input()) for i in range(n)]
chk = [[False for i in range(n)] for i in range(n)]
recp_li = copy.deepcopy(li)
recp_chk = [[False for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if recp_li[i][j] == "G":
            recp_li[i][j] = "R"
def dfs(x,y,color,li,chk):
    chk[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if li[nx][ny] == color and chk[nx][ny] == False:
                dfs(nx,ny,color,li,chk)
def main(n,li,chk):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if chk[i][j] == False:
                dfs(i,j,li[i][j],li,chk)
                cnt += 1
    return cnt
print(main(n,li,chk),end=' ')
print(main(n,recp_li,recp_chk))
