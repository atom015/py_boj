def func(ix,cnt):
    if cnt == m:
        for i in li:
            print(i,end=' ')
        print()
    else:
        for i in range(len(arr)):
            li[cnt] = arr[i]
            func(i+1,cnt+1)
n,m = map(int,input().split())
li = [0 for i in range(m)]
arr = [i+1 for i in range(n)]
func(0,0)
