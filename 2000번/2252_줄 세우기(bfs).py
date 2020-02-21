import sys
ip = sys.stdin.readline
n,m = map(int,ip().split())
inDegree = [0 for _ in range(n+1)]
arr = [[] for _ in range(n+1)]
def topologySort():
    q = []
    #진입차수가 0인 노드를 큐에 삽입합니다.
    for i in range(1,n+1):
        if inDegree[i] == 0:q.append(i)
    # 정렬이 완전히 수행되려면 정확히 n개의 노드를 방문합니다.
    while q:
        p = q.pop(0)
        print(p,end=' ')
        for i in arr[p]:
            inDegree[i] -= 1
            if inDegree[i] == 0:
                q.append(i)
for i in range(m):
    a,b = map(int,ip().split())
    arr[a].append(b)
    inDegree[b] += 1
topologySort()
