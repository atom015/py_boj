import sys
ip = sys.stdin.readline
n,m,k = map(int,ip().split())
a = [int(ip()) for i in range(n)]
tree = [0]*(4*n)
def init(s,e,nd):
    if s == e:#만약에 시작 인덱스와 끝인덱스가 같으면 tree[nd]에 a의 시작인덱스를 넣어놓고 return해준다.
        tree[nd] = a[s]
        return tree[nd]
    m = (s+e)//2
    #재귀적으로 두 부분으로 나눈 뒤에 그 합을 자기자신으로 합니다.
    #tree의 현재노드에 자신의 자식노드인 nd*2,nd*2+1을 값을 더해서 넣어준다.
    tree[nd] = init(s,m,nd*2)+init(m+1,e,nd*2+1) #반씩나눠서 더해준다
    return tree[nd]
#s:시작인덱스,e:끝인덱스
#l,r:구간 합을 구하고자 하는 범위
def Sum(s,e,nd,l,r):
    #범위 밖에 있는경우
    if l > e or r < s:return 0
    #범위 안에 있는경우
    if l <= s and e <= r:return tree[nd]
    #그맇지 않다면 두 부분으로 나누어 합을 구하기
    m = (s+e)//2
    tmp = Sum(s,m,nd*2,l,r)+Sum(m+1,e,nd*2+1,l,r)
    return tmp
def update(n,s,e,t,dif):
    if s <= t and t <= e:
        tree[n] += dif
    else:
        return
    if s == e:
        return
    m = (s+e)//2
    update(n*2,s,m,t,dif)
    update(n*2+1,m+1,e,t,dif)

init(0,n-1,1)
for i in range(m+k):
    t,b,c = map(int,ip().split())
    if t == 1:
        dif = c-a[b-1]
        a[b-1] = c
        update(1,0,n-1,b-1,dif)
    else:
        print(Sum(0,n-1,1,b-1,c-1))
