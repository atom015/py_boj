board = [[0 for _ in range(101)] for _ in range(101)]
cnt = 0
for _ in range(int(input())):
    x,y = map(int,input().split())
    i = y+1
    while i <= y+10:
        j = x+1
        while j <= x+10:
            board[i][j] = 1
            j += 1
        i += 1
for i in range(101):
    for j in range(101):
        if board[i][j] == 1:
            cnt += 1
print(cnt)

