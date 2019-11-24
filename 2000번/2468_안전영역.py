n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
ret = 0

def copy_the_array(val):
    v = [[False for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= val:
                arr[i][j] = -1
                v[i][j] = True
    return v,arr

def node_connection(x,y):
    v[x][y] = True
    q = [[x,y]]
    while q:
        x,y = q.pop(0)
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            nx,ny = dx+x,dy+y
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] != -1 and not(v[nx][ny]):
                    q.append([nx,ny])
                    v[nx][ny] = True

for k in range(101):
    v,arr = copy_the_array(k)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != -1 and not(v[i][j]):
                node_connection(i,j)
                cnt += 1
    if cnt == 0:break
    ret = max(ret,cnt)
print(ret)
