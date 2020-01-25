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
