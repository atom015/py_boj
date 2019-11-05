import sys
import queue as Q
ip = sys.stdin.readline
n = int(ip()) #n개의 도시
m = int(ip()) #한도시에서 출발하여 다른도시에 도착하는 버스 M개
arr = [[] for i in range(n+1)]
d = [1e9]*(n+1)
for i in range(m):
    a,b,c = map(int,ip().split())
    arr[a].append([b,c])
s,e = map(int,ip().split())
def dijkstra(s):
    q = Q.PriorityQueue()
    q.put((0,s))
    d[s] = 0
    while not q.empty():
        p = q.get()
        nd = p[1]
        dist = p[0]
        if d[nd] < dist:
            continue
        for i in arr[nd]:
            cost = dist+i[1]
            if d[i[0]] > cost:
                d[i[0]] = cost
                q.put((cost,i[0]))
dijkstra(s)
print(d[e])
#일반 다익스트라 알고리즘에서 최소비용[끝도시]를 출력해주면된다.
