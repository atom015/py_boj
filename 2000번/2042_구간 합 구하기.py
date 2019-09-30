import sys
ip = sys.stdin.readline
n,m,k = map(int,ip().split())
a = [int(ip()) for i in range(n)]
tree = [0]*(4*n)
def init(s,e,nd):
    if s == e: #이경우에는 node가 리프노드(자식이 없는노드)인경우 이기 때문에 배열의 그원소를 가져야한다
        tree[nd] = a[s]
        return tree[nd]
    m = (s+e)//2
    #재귀적으로 두 부분으로 나눈 뒤에 그 합을 자기자신으로 합니다.
    #tree의 현재노드에 자신의 자식노드인 nd*2,nd*2+1을 값을 더해서 넣어준다.
    tree[nd] = init(s,m,nd*2)+init(m+1,e,nd*2+1) #인덱스를 반씩나눠서 더해준다
    return tree[nd]
#s:시작인덱스,e:끝인덱스
#l,r:구간 합을 구하고자 하는 범위
#1.[left,right]와 [start,end]가 겹치지 않는 경우
#2.[left,right]가 [start,end]를 완전히 포함하는 경우
#3.[start,end]가 [left,right]를 완전히 포함하는 경우
#4.[left,right]와 [start,end]가 겹쳐져 있는 경우 (1, 2, 3 제외한 나머지 경우)
def Sum(s,e,nd,l,r):
    #리스트 밖에 구하고자하는 범위가 있는경우
    if l > e or r < s:return 0 #l > e경우 l,r뒤에 있는경우,r < s경우 l,r앞에 있는경우이다 겹치지 않으므로 0을 리턴한다.
    #범위 안에 있는경우
    if l <= s and e <= r:return tree[nd]#구해야하는 합의 범위는 l,r인데,s,e는 그 범위에 모두 포함되고, 그 node의 자식도 모두 포함되기 때문에 tree[node]를 리턴한다.
    #그맇지 않다면 두 부분으로 나누어 합을 구하기
    m = (s+e)//2
    tmp = Sum(s,m,nd*2,l,r)+Sum(m+1,e,nd*2+1,l,r)
    return tmp
#1.[start,end]에 index가 포함되는 경우
#2.[start,end]에 index가 포함되지 않는 경우
def update(n,s,e,t,dif):
    if s <= t and t <= e: #1번의 경우 tree의 현재노드에 +dif만큼해준다.
        tree[n] += dif
    else: #2번의 경우 return
        return
    if s == e: #노드가 리프노드이면 return
        return
    m = (s+e)//2
    update(n*2,s,m,t,dif)
    update(n*2+1,m+1,e,t,dif)

init(0,n-1,1)
for i in range(m+k):
    t,b,c = map(int,ip().split())
    if t == 1:
        dif = c-a[b-1] #index번째 수를 val로 변경한다면, 그 수가 얼마만큼 변했는지를 알아야 하니까 diff = val - a[index]로 쉽게 구할 수 있다.
        a[b-1] = c
        update(1,0,n-1,b-1,dif)
    else:
        print(Sum(0,n-1,1,b-1,c-1))
#참고:https://www.acmicpc.net/blog/view/9
