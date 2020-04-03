from itertools import combinations
ans = []
for i in range(int(input())):
    arr = list(map(int,input().split()))
    tmp = 0
    for i in combinations(arr,3):
        tmp = max(sum(i)%10,tmp)
    ans.append(tmp)
ret = [i if ans[i] == max(ans) else -1 for i in range(len(ans))]
print(max(ret)+1)
