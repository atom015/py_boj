n = int(input())
Node = list(map(int,input().split()))
delete = int(input())
ans = 0
arr = [[] for i in range(n)]
v = [False for i in range(n)]
q = []
for i in range(n):
    if Node[i] == -1:
        q.append(i)
        v[i] = True
    else:
        arr[Node[i]].append(i)
if q[0] != delete:
    v[delete] = True
    while q:
        child_node = 0
        node = q.pop(0)
        for i in arr[node]:
            if v[i] == False:
                child_node += 1
                q.append(i)
                v[i] = True
        if child_node == 0:
            ans += 1
print(ans)
