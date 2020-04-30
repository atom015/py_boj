import sys
sys.setrecursionlimit(50000) #재귀제한높이설정(이걸 기본값이상으로 안해주면 런타임에러가 난다.) ※기본값:1000
n,m,k = map(int,input().split()) #n:통로의세로길이,m:통로의가로길이,k:음식물쓰레기개수
li = [[0 for i in range(m)] for i in range(n)] #인접행렬을 가로길이:m,세로길이:n으로 만들어준다.
#상하좌우비교 리스트
dx = [0,0,-1,1]
dy = [1,-1,0,0]
compare = 0 #가장큰 음식물크기 비교 변수
#입력
for i in range(k):
    a,b = map(int,input().split())
    li[a-1][b-1] = 1
def dfs(x,y):
    global cnt
    cnt += 1 #음식물크기를 늘려준다.
    li[x][y] = 0 #방문체크
    #상하좌우
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m: #nx,nx가 지도를 벗어나지않고
            if li[nx][ny] == 1: #방문한적이없으면
                dfs(nx,ny) #재귀를 돌린다.
    return cnt #cnt반환
for i in range(n):
    for j in range(m):
        if li[i][j] == 1:
            cnt = 0 #1이있을때마다 cnt를 초기화시켜준다.
            func = dfs(i,j) #func에 음식물크기를넣어준다.
            if compare < func: #만약에 func에들어있는값이 비교하는값에 들어있는값보다 클경우 서로 compare에 func를 넣어준다.
                compare = func
print(compare) #가장큰 음식물크기 출력
