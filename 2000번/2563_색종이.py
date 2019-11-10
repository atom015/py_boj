board = [[0 for _ in range(101)] for _ in range(101)]
cnt = 0
for _ in range(int(input())):
    x,y = map(int,input().split())
    for i in range(y+1,y+11):
        for j in range(x+1,x+11):
            board[i][j] = 1
for i in range(101):
    for j in range(101):
        if board[i][j] == 1:
            cnt += 1
print(cnt)

