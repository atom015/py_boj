from sys import *
ip = stdin.readline
arr = [list(map(int,ip().split())) for i in range(9)]
R = [[0]*10 for i in range(9)]
C = [[0]*10 for i in range(9)]
Sq = [[0]*10 for i in range(9)]
d = lambda x,y:(x//3)*3+(y//3)
for i in range(9):
    for j in range(9):
        if arr[i][j] != 0:
            R[i][arr[i][j]] = 1
            C[j][arr[i][j]] = 1
            Sq[d(i,j)][arr[i][j]] = 1
def dfs(cnt):
    x,y = cnt//9,cnt%9
    if cnt == 81:
        for i in arr:
            print(*i)
        exit()
    if arr[x][y] == 0:
        for i in range(1,10):
            if not R[x][i] and not C[y][i] and not Sq[d(x,y)][i]:
                R[x][i] = 1
                C[y][i] = 1
                Sq[d(x,y)][i] = 1
                arr[x][y] = i
                dfs(cnt+1)
                arr[x][y] = 0
                R[x][i] = 0
                C[y][i] = 0
                Sq[d(x,y)][i] = 0
    else: dfs(cnt+1)
dfs(0)
