def gp(p,x):
    if p[x] == x:
        return p[x]
    p[x] = gp(p,p[x])
    return p[x]
def up(a,b):
    a = gp(p,a)
    b = gp(p,b)
    if a < b:
        p[b] = a
    else:
        p[a] = b
def ch(a,b):
    a = gp(p,a)
    b = gp(p,b)
    if a == b:
        return True
    return False
n = int(input())
m = int(input())
p = [i for i in range(n+1)]
arr = []
ans = 0
for i in range(m):
    a,b,c = map(int,input().split())
    arr.append([a,b,c])

arr.sort(key=lambda x:(x[2]))
for i in range(m):
    if ch(arr[i][0],arr[i][1]) == False:
        up(arr[i][0],arr[i][1])
        ans += arr[i][2]
print(ans)
