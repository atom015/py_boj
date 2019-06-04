n,m = map(int,input().split())
def push(x):
    Queue.append(x)
def size():
    return len(Queue)
Queue = []
chk = [[False for i in range(m)] for i in range(n)]
li = [[int(i) for i in list(input())] for i in range(n)]
push([0,0,1])
chk[0][0] = True
while size() != 0:
    p = Queue.pop(0)
    x,y,cnt = p[0],p[1],p[2]
    # print(x,y)
    if x == m-1 and y == n-1:
        print(cnt)
        break
    if x+1 < m and li[y][x+1] == 1 and chk[y][x+1] == False:
        push([x+1,y,cnt+1])
        chk[y][x+1] = True
    if x-1 >= 0 and li[y][x-1] == 1 and chk[y][x-1] == False:
        push([x-1,y,cnt+1])
        chk[y][x-1] = True
    if y+1 < n and li[y+1][x] == 1 and chk[y+1][x] == False:
        push([x,y+1,cnt+1])
        chk[y+1][x] = True
    if y-1 >= 0 and li[y-1][x] == 1 and chk[y-1][x] == False:
        push([x,y-1,cnt+1])
        chk[y-1][x] = True
