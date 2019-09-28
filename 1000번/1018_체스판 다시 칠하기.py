def f(i,j):
    global ans
    chcolor = ["B","W"]
    for a in range(2):
        cnt = 0
        for b in range(i,i+8):
            for c in range(j,j+8):
                if board[b][c] != chcolor[a%2]:
                    cnt += 1
                a += 1
            a += 1
        if cnt < ans:
            ans = cnt
n,m = map(int,input().split())
board = [input() for i in range(n)]
ans = 1e9
for i in range(n-7):
    for j in range(m-7):
        f(i,j)
print(ans)
