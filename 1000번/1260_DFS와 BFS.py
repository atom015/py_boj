"""
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1
1 2 4 3
1 2 3 4
예제 입력 2
5 5 3
5 4
5 2
1 2
3 4
3 1
예제 출력 2
3 1 2 5 4
3 1 4 2 5
예제 입력 3
1000 1 1000
999 1000
예제 출력 3
1000 999
1000 999
"""
n,m,start = map(int,input().split()) #N:node의 개수,M:간선의 개수,start:시작노드
li = [[0 for i in range(n)] for i in range(n)] # li으로 인접행렬 만들기
visited = [False for i in range(n)] #방문한 노드 체크
Queue = [start] #Queue에 시작할노드를 넣는다.
def dfs(nd,n): #함수에 매개변수로 현재노드와 node의 개수를 받는다.
    print(nd+1,end=' ') #인덱스를 맞추기위해 1을 빼고 넣었기때문에 1을더하고 출력해준다.
    visited[nd] = True #visited에 현재노드를 True로 바꿔준다.
    for i in range(n):
        if li[nd][i] == 1 and visited[i] == False: #만약에 현재노드에 i번째 값이 1이고 방문한적이 없으면
            dfs(i,n) #재귀함수에 i,n을 넣어서 돌린다.
#인접행렬으로 받기
for i in range(m):
    a,b = map(int,input().split())
    li[a-1][b-1] = 1
    li[b-1][a-1] = 1
dfs(start-1,n) #첫 dfs함수 호출
print()
visited = [False for i in range(n)] #위에서 visited이 바뀌었기때문에 초기화 해준다.
while len(Queue) != 0: #Queue가 비었을때까지 while문을 돈다.
    p = Queue.pop(0)-1 #이것도 인덱스를 맞추기위해서 pop한값에 1을 빼준다.
    print(p+1,end=' ')
    visited[p] = True #방문 체크
    for i in range(n):
        if li[p][i] == 1 and visited[i] == False: #만약에 pop한값에 i번째 값이 1이고 방문하지않았으면
            visited[i] = True #방문체크
            Queue.append(i+1) #Queue에 append
