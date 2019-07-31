n = int(input())
result = []
li = []
for i in range(n):
    a,b,c = map(int,input().split())
    li.append([a,b,c])

def compare(nd,nv,ln):
    for i in range(len(li)):
        if i != ln and li[i][nd] == nv:
            return False
        else:
            continue
    return True

for i in range(n):
    cnt = 0
    for j in range(3):
        if compare(j,li[i][j],i) == True:
            cnt += li[i][j]
    result.append(cnt)
for i in result:
    print(i)
