import queue as Q
import sys
ip = sys.stdin.readline
v,e = map(int, ip().split())
s = int(input())

adj = [[] for i in range (v+1)] #인접리스트
#[[],[(2, 2), (3, 3)], [(3, 4), (4, 5)], [(4, 6)], [], [(1, 1)]]
ans = [10000000]*(v+1) #최소비용
for i in range(e):
    a, b, c = map(int,ip().split())
    adj[a].append((b,c))

def dijkstra(s):
    q = Q.PriorityQueue() #우선순위큐(넣는 순서는 상관없지만 나올때는 가장 작은 값부터 나온다는 특징이있다.)
    q.put((0,s)) #큐에 초기비용,시작점을 넣어준다.
    ans[s] = 0 #시작지점은 0으로 넣어준다.
    while not q.empty(): # q가 비어있지않았다면
        # (0, 1)
        # (2, 2)
        # (3, 3)
        # (7, 4)
        pp = q.get() #큐의 작은값 pop
        here = pp[1] #노드
        dist = pp[0] #비용
        if ans[here] < dist: #ans[here]에있는 비용이 dist보다 작으면 continue
            continue
        for i in adj[here]:
            cost = dist + i[1] #현재노드+연결되어있는노드로 가는비용
            if ans[i[0]] > cost: #연결되어있는노드의 현재 비용 > 현재노드비용+연결되어있는노드로 가는 비용
                #비용갱신
                ans[i[0]] = cost
                q.put((cost, i[0])) #노드에 나온 최소비용과 노드번호를 q에 넣어준다.
dijkstra(s)

for i in range (1,v+1):
    print("INF" if d[i] == 1e9 else d[i]) #만약에 갈수없으면 INF출력 아니면 그냥출력
