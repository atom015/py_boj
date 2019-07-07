#세로를구해준다.
def le(li,n):
    tmp1 = [[] for i in range(n)]
    #tmp1에 각각의세로값들을 넣어준다.
    for i in range(n):
        for j in range(n):
            tmp1[j].append(li[i][j])
    #그다음 2차원리스트로 되어있는것을 join으로 다 하나의 문자열로만들어준다.
    tmp2 = ["".join(i) for i in tmp1]
    return tmp2
n = int(input()) #방의크기
w,l = 0,0 #가로와 세로의 누울수있는 자리의개수
width = [input() for i in range(n)] #가로를 입력받는다.
length = le(width,n) #세로를 구해주기위해 아까 만들어준 함수로 구해준다.
for i in range(n):
    wc,lc = 0,0
    for j in range(n):
        if width[i][j] == ".": #만약에 width[i][j]가 비어있으면 wc에 1을더해준다.
            wc += 1
        else: #만약에 비어있지 않으면 다시 초기화시켜준다.
            wc = 0
        if wc == 2: #누을수있는 칸은 2칸이상이므로 2칸이면
            w += 1 #누울수있는 가로칸에 1을더해준다.
        if length[i][j] == ".": #세로에 빈칸이 있으면 lc에 1을 더해준다.
            lc += 1
        else: #비어있으면 다시초기화 시켜준다.
            lc = 0
        if lc == 2: #누을수있는 칸은 2칸이상이므로 2칸이면
            l += 1 #누울수있는 세로칸에 1을더해준다.
print(w,l) #누울수있는 가로칸 세로칸 출력
