com = int(input()) #컴퓨터수
net = int(input()) #네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
li = [[0 for i in range(com)] for i in range(com)] #컴퓨터랑 컴퓨터가 연결되어있는걸 체크하기위해 인접행렬을 com * com으로 만들어준다.
visted = [False for i in range(com)] #특정 컴퓨터를 방문한걸 체크하기위해 만들어줌
#입력
for i in range(net):
    a,b = map(int,input().split())
    li[a-1][b-1] = 1
    li[b-1][a-1] = 1
cnt = 0 #바이러스가 걸리는 컴퓨터수 체크
def dfs(nd,com):
    global cnt
    nd = nd-1 #리스트 인덱스를 맟추기위해서 1을 빼준다.
    visted[nd] = True #현재노드 방문체크
    for i in range(com): #현재노드에 인덱스를 모두돌기위해 인접행렬에 가로길이인 컴퓨터수만큼 돈다.
        if li[nd][i] == 1 and visted[i] == False: #만약에 인접행렬에 현재노드에 i번째 값이 1이고 한번도 방문한적이없으면
            cnt += 1 #컴퓨터수를 세주고
            dfs(i+1,com) #재귀를돈다.
dfs(1,com)
print(cnt) #바이러스가 걸리는 컴퓨터수 출력
