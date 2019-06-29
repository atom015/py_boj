n = int(input())
li = [list(input()) for i in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
result = []
def dfs(x,y):
    global cnt
    li[x][y] = '0'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < n and nx >= 0 and ny < n and ny >= 0 and li[nx][ny] == '1':
            cnt += 1
            dfs(nx,ny)
    return cnt

for i in range(n):
    for j in range(n):
        if li[i][j] == '1':
            cnt = 1
            result.append(dfs(i,j))
print(len(result))
for i in sorted(result):
    print(i)
