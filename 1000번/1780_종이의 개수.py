n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
ans = [0,0,0]
def checking(size,x,y):
    for i in range(x,x+size):
        for j in range(y,y+size):
            if arr[i][j] != arr[x][y]:
                return False
    return True
def Division(x,y,size):
    if checking(size,x,y):
        ans[arr[x][y]+1] += 1
    else:
        div = size//3
        for i in range(3):
            for j in range(3):
                Division(x+div*i,y+div*j,div)

Division(0,0,n)
for i in ans:
    print(i)
