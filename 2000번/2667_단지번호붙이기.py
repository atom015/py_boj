n = int(input())
li = [[int(i) for i in list(input())] for i in range(n)]
result =[]
def dfs(x,y):
    global cnt
    li[x][y] = 0
    for i in range(4):
        if x+1 < n and li[x+1][y] == 1:
            dfs(x+1,y)
            cnt += 1
        if x-1 >= 0 and li[x-1][y] == 1:
            dfs(x-1,y)
            cnt += 1
        if y+1 < n and li[x][y+1] == 1:
            dfs(x,y+1)
            cnt += 1
        if y-1 >= 0 and li[x][y-1] == 1:
            dfs(x,y-1)
            cnt += 1
    return cnt
for i in range(n):
    for j in range(n):
        if li[i][j] == 1:
            cnt = 1
            result.append(dfs(i,j))
print(len(result))
for i in sorted(result):
    print(i)
