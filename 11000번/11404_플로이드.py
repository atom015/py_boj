import sys
ip = sys.stdin.readline
n = int(ip())
m = int(ip())
inf = 1e9
#배열 초기화
d = [[inf for i in range(n)] for i in range(n)]
#자기자신은 0으로 해준다.
for i in range(n):
    d[i][i] = 0
def floydWarshall():
    #k:거쳐가는 노드
    for k in range(n):
        #i:출발노드
        for i in range(n):
            #j:도착노드
            for j in range(n):
                d[i][j] = min(d[i][k]+d[k][j],d[i][j]) #현재 노드의 가중치(d[i][j])보다 거쳐가는 노드의 가중치(d[i][k]+d[k][j])가 더작다면 갱신
    for i in range(n):
        for j in range(n):
            if d[i][j] == 1e9: #만약에 갈수없으면 0출력
                print(0,end=' ')
            else:
                print(d[i][j],end=' ')
        print()
for i in range(m):
    a,b,c = map(int,ip().split())
    d[a-1][b-1] = min(d[a-1][b-1],c) #가중치 값이 2번들어 올수도 있기때문에 현재가중치이랑 들어온 가중치랑 비교해서 작은값을 넣어준다.
floydWarshall()
