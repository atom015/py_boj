n = int(input())
arr = list(map(int,input().split()))
s = sum(arr)
ch = [0 for i in range(s+1)]

def dfs(i,w):
    ch[w] = 1
    if i >= n:
        return
    dfs(i+1,w)
    dfs(i+1,w+arr[i])
    dfs(i+1,abs(w-arr[i]))

dfs(0,0)
print(ch.count(0))
