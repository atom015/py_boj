import sys
sys.setrecursionlimit(50000) #재귀제한높이설정(이걸 기본값이상으로 안해주면 런타임에러가 난다.) ※기본값:1000
def dfs(x,y):
    li[x][y] = 0 #chk함수대신에 인접행렬에 직접표시
    #상하좌우
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and li[nx][ny] == 1: #nx,ny가 지도를 안벗어나고 방문한적이없으면 재귀를돈다.
            dfs(nx,ny)
#상하좌우비교 리스트
dx = [1,0,-1,0]
dy = [0,-1,0,1]
for i in range(int(input())): #테스트케이스 입력
    m,n,k = map(int,input().split()) #M:가로길이,N:세로길이,K:위치개수
    li = [[0 for i in range(m)] for i in range(n)] #인접행렬
    for i in range(k):
        a,b = map(int,input().split())
        li[b][a] = 1
    cnt = 0 #배추흰지렁이 마리수
    #이중포문을 돌면서 1이있으면 주변에있는1들을 체크하고 다0으로 바꿔준후 배추흰지렁이수를 늘려준다.
    for i in range(n):
        for j in range(m):
            if li[i][j] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt) #배추흰지렁이 수출력
