n,m = map(int,input().split())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
Queue = []
chk = [[False for i in range(m)] for i in range(n)]
li = [list(input()) for i in range(n)]
Queue.append([0,0,1])
chk[0][0] = True
while len(Queue) != 0:
    p = Queue.pop(0)
    x,y,cnt = p[0],p[1],p[2]
    if y+1 == n and x+1 == m:
        print(cnt)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if li[ny][nx] == '1' and chk[ny][nx] == False:
                Queue.append([nx,ny,cnt+1])
                chk[ny][nx] = True
