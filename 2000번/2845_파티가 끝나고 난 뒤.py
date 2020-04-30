l,p = map(int,input().split())
a = list(map(int,input().split()))
ans = l*p
for i in a:
    print(i-ans,end=' ')
