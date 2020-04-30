t = int(input())
n = list(map(int,input().split()))
sli = []
for i in range(t):
    sli.insert(i- n[i],i+1)
for i in sli:
    print(i,end=' ')
