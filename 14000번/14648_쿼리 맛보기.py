n,q = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(q):
    s = list(map(int,input().split()))
    if s[0] == 2:
        a,b,c,d = s[1],s[2],s[3],s[4]
        print(sum(arr[a-1:b])-sum(arr[c-1:d]))
    else:
        a,b = s[1],s[2]
        print(sum(arr[a-1:b]))
        arr[a-1],arr[b-1] = arr[b-1],arr[a-1]
