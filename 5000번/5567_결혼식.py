n = int(input()) #상근이의 동기의 수
m = int(input()) #리스트의 길이
friend = [False for i in range(n+1)] #친구수체크 리스트
li = [[] for i in range(n+1)] #인접리스트
#인접리스트 채우기
for i in range(m):
    a,b = map(int,input().split())
    li[a].append(b)
    li[b].append(a)
def dfs(nd):
    #친구의 친구 체크
    for i in range(len(li[nd])): #현재노드에 값이있는 길이만큼돈다.
        tmp = li[nd][i] #값을 tmp에저장한후
        friend[tmp] = True #친구체크
    if nd == 1: #처음친구 체크
        for i in range(len(li[nd])): #현재노드에 값이있는 길이만큼돈다.
            tmp = li[nd][i] #tmp에 현재값저장
            dfs(tmp) #재귀
dfs(1) #처음에 상근이에 번호는 1번이니까 처음시작은 1로해준다.
print(friend.count(True)-1) #True가있는곳은 상근이의 친구,친구의친구가 있는곳이니까 count Ture를 해주고 자신은 체크하면 안되니까 1을빼줘서 출력해준다.
