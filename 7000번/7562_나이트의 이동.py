dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]
def bfs(a,n,x,y,ex,ey):
    q = []
    visited = [[False for i in range(n)] for i in range(n)]
    visited[x][y] = True
    q.append([x,y,0])
    while len(q) != 0:
        x,y,cnt = q.pop(0)
        if x == ex and y == ey:
            return cnt
        for i in range(8):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append([nx,ny,cnt+1])
    return cnt
for i in range(int(input())):
    I = int(input())
    n,n1 = map(int,input().split())
    go,go2 = map(int,input().split())
    a = [[0 for i in range(I)] for i in range(I)]
    print(bfs(a,I,n,n1,go,go2))
