n = int(input()) #지도의 크기
li = [list(input()) for i in range(n)] #지도의 크기는 가로세로가 같으므로 이런식으로 만들어줬다.
#상하좌우 비교 리스트
dx = [-1,0,1,0]
dy = [0,1,0,-1]
result = [] #단지들의 집수
def dfs(x,y):
    global cnt
    cnt += 1 #집들의수를 세준다
    li[x][y] = '0' #방문했다고 체크해준다
    for i in range(4):
        nx = x + dx[i] #좌우
        ny = y + dy[i] #상하
        if 0 <= nx < n and 0 <= ny < n and li[nx][ny] == '1': #만약에 nx,ny값이 지도밖을 안벗어나고 nx,nx값이 1이면
            dfs(nx,ny) #재귀를돌려준다
    return cnt #집수를 리턴해준다.
#for문을돌면서 1이있으면 cnt를 초기화시켜주고 집수를 result에 append해준다.
for i in range(n):
    for j in range(n):
        if li[i][j] == '1':
            cnt = 0
            result.append(dfs(i,j))
print(len(result)) #단지수출력
for i in sorted(result): #sort된 집수 출력
    print(i)
