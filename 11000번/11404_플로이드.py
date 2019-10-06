import sys
ip = sys.stdin.readline
n = int(ip())
m = int(ip())
inf = 1e9
arr = [[inf for i in range(n)] for i in range(n)]
for i in range(n):
    arr[i][i] = 0
def floydWarshall():
    d = arr
    #k:거쳐가는 노드
    for k in range(n):
    #i:출발노드
        for i in range(n):
            #j:도착노드
            for j in range(n):
                d[i][j] = min(d[i][k]+d[k][j],d[i][j])
    for i in range(n):
        for j in range(n):
            if d[i][j] == 1e9:
                print(0,end=' ')
            else:
                print(d[i][j],end=' ')
        print()
for i in range(m):
    a,b,c = map(int,ip().split())
    arr[a-1][b-1] = min(arr[a-1][b-1],c)
floydWarshall()
