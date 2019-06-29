n,m = map(int,input().split()) #n:세로길이,m:가로길이
#상하좌우비교 리스트
dx = [0,1,0,-1]
dy = [1,0,-1,0]
Queue = []
chk = [[False for i in range(m)] for i in range(n)] #방문했는지안했는지 확인하는 체크리스트를 만들어준다.
li = [list(input()) for i in range(n)] #인접행렬
Queue.append([0,0,1]) #큐에 현재 x좌표 y좌표를 넣어준다
chk[0][0] = True #방문처리
while len(Queue) != 0: #큐가 빌때까지 돈다.
    p = Queue.pop(0) #큐에서 하나의 값을 뽑는다.
    x,y,cnt = p[0],p[1],p[2] #pop한값은 리스트로 되어있으니 0번째는 x 1번째는 y이런식으로 저장해준다.
    if y+1 == n and x+1 == m: # 만약에 결괴값이랑 xy값이랑 같으면
        print(cnt) #미로 탐색수를 출력하고 끝낸다.
        break
    for i in range(4): #상하좌우비교
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n: #만약에 nx,ny가 지도를 안넘고
            if li[ny][nx] == '1' and chk[ny][nx] == False: #li의 li[ny][nx]부분에 길이있고 방문하지않았으면
                Queue.append([nx,ny,cnt+1]) #큐에넣어주고
                chk[ny][nx] = True #방문표시해준다.
