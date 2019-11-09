n = int(input())
arr = list(map(int,input().split()))
ret = [arr[0]]
for i in range(1,n):
    ret.append((arr[i]*(i+1))-sum(ret))
for i in range(n):
    print(ret[i],end=' ')