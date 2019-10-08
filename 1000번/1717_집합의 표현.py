import sys
ip = sys.stdin.readline
#재귀함수를 통해 부모노드를 찾고 부모노드를 갱신한다.
def getP(p,x):
    if p[x] == x:
        return x
    p[x] = getP(p,p[x])
    return p[x]
#두노드를 비교하고 더작은 부모노드를 두개의노드의 부모노드로 만든다.
def union(p,a,b):
    a = getP(p,a)
    b = getP(p,b)
    if a < b:
        p[b] = a
    else:
        p[a] = b
#두 원소가 같은 집합에 포함되어 있는지를 확인한다.
def findP(p,a,b):
    a = getP(p,a)
    b = getP(p,b)
    #두 부모노드가 같으면 YES출력 아니면 NO출력
    if a == b:
        return "YES"
    return "NO"
n,m = map(int,ip().split())
p = [i for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,ip().split())
    if a == 0:
        union(p,b,c)
    else:
        print(findP(p,b,c))
