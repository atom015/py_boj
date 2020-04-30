import sys,copy
sys.setrecursionlimit(500000) #런타임에러가 안나게 재귀재한깊이를 늘려준다.
n = int(input())
#상하좌우 비교 리스트
dx = [1,0,-1,0]
dy = [0,-1,0,1]
li = [list(input()) for i in range(n)] # N*N이니까 str리스트로 받아주고 n번만큼 돈다.
chk = [[False for i in range(n)] for i in range(n)] #N*N으로 chk리스트를 만들어준다.
recp_li = copy.deepcopy(li) #그냥 카피하면 적록색약리스트 바꿔주면 li도 바뀌기 때문에 모듈을 써줬다.
recp_chk = [[False for i in range(n)] for i in range(n)] #chk처럼 N*N으로 적록색약 chk를 만들어줬다.
#적록색약은 빨강이랑 초록이랑 같은색으로 보기때문에 G(초록)을 R(빨강)이랑 같은색으로 바꿔줬다.
for i in range(n):
    for j in range(n):
        if recp_li[i][j] == "G":
            recp_li[i][j] = "R"
def dfs(x,y,color,li,chk):
    chk[x][y] = True #방문체크를해준다.
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n: #만약에 상하좌우비교한게 지도를 안벗어나고
            if li[nx][ny] == color and chk[nx][ny] == False: #들어온색깔이랑같고 방문한적이없으면
                dfs(nx,ny,color,li,chk) #재귀를돈다.
def main(n,li,chk):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if chk[i][j] == False:
                dfs(i,j,li[i][j],li,chk)
                cnt += 1
    return cnt
print(main(n,li,chk),end=' ')
print(main(n,recp_li,recp_chk))
#원래는 귀찮게 두번씩해야했는데 함수로 두번 매개변수로 넣어서 코드길이를 줄여줬다.
