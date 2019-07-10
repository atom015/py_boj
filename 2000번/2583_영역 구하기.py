import sys
sys.setrecursionlimit(50000) #런타임에러가안나게 기존재귀 깊이값이 아닌 좀더늘린 50000으로 설정해준다.
m,n,k = map(int,input().split()) #m:세로,n:가로,k:좌표의 개수
#상하좌우 비교 리스트
dx = [1,0,-1,0]
dy = [0,-1,0,1]
li = [[0 for i in range(n)] for i in range(m)] #m(세로)*n(가로)으로 인접행렬을 만들어줬다.
visited = [[False for i in range(n)] for i in range(m)] #m(세로)*n(가로)으로 방문체크 리스트를 만들어준다.
result = [] #넓이들을 넣어준다.
for i in range(k):
    x1,y1,x2,y2 = map(int,input().split()) #x1,y1:직사각형의 왼쪽아래 꼭짓점 x,y좌표값 x2,y2:직사각형의 오른위꼭짓점 좌표값 ,예:1,1,2,5
    for y in range((m-y2),(m-y1),1): #(세로-y2)부터 (세로-y1)까지 1씩늘어나게 한다. 예:(5-1,5-1),(4,4,1)
        for x in range(x1,x2,1): #x1부터 x2까지 1씩늘어나게 한다.(2,5,1)
            li[y][x] = 1 #li[y][x]를 1로 바꿔준다.
            visited[y][x] == True #1이된부분을 dfs에서 방문하면안되니까 같아 방문처리를 해주었다.
def dfs(x,y):
    global cnt
    cnt += 1 #넓이를 구하기위해 1씩더해준다.
    visited[x][y] = True #방문체크
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n: #만약에 상하좌우비교 값이 지도밖을 벗어나지 않고
            if li[nx][ny] == 0 and visited[nx][ny] == False: #li[nx][ny]가 0이고 방문한적이없으면
                dfs(nx,ny) #재귀
    return cnt #cnt를 반환
#만약에 li[i][j]가 0이고 방문한적이 없으면 dfs를 돌린다.
for i in range(m):
    for j in range(n):
        if li[i][j] == 0 and visited[i][j] == False:
            cnt = 0
            result.append(dfs(i,j))
print(len(result)) #영역의 개수출력
for i in sorted(result): #오름차순으로 각 영역의 넓이 출력
    print(i,end=' ')
