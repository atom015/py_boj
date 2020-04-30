import sys
sys.setrecursionlimit(500000) #런타임에러가 나지않도록 재귀제한깊이를 늘려줬다.
#상하좌우 대각선까지 비교리스트
dx = [0,1,-1,0,1,-1,-1,1]
dy = [1,0,0,-1,1,1,-1,-1]
def dfs(x,y):
    chk[x][y] = True #방문체크
    for i in range(8): #상,하,좌,우,대각선을 돌아서 총 8번돈다.
        #상하좌우 대각선 비교
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w: #만약에 상하좌우 대각선비교값이 지도밖을 안벗어나고
            if li[nx][ny] == 1 and chk[nx][ny] == False: #상하좌우 대각선비교값에 섬이있고 방문한적이없으면
                dfs(nx,ny) #재귀를 돈다.
while 1:
    w,h = map(int,input().split()) #너비와 높이를 입력받는다.
    if w == 0 and h == 0: #너비와 높이가 0이면 while문을 끝낸다.
        break
    li = [list(map(int,input().split())) for i in range(h)] #W*H로 인접행렬을 만들어준다.
    chk = [[False for i in range(w)] for i in range(h)] #W*H로 방문체크 인접행렬을 만들어준다.
    cnt = 0 #섬의개수 체크변수
    #이중포문을 돌면서 만약에 섬이있고 방문한적이없으면 dfs를 돈다.
    for i in range(h):
        for j in range(w):
            if li[i][j] == 1 and chk[i][j] == False:
                cnt += 1 #섬의 개수체크
                dfs(i,j)
    print(cnt) #결과 출력
#참고※백준 유기농배추(1012번)에서 대각선만 추가한 문제이다.
