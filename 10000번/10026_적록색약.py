"""
문제
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

예제 입력 1
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
예제 출력 1
4 3
"""
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
