import itertools
def func(n):
    ans = ""
    for i in n:
        ans += str(i)
    return int(ans)

n = list(map(int,input()))
arr = sorted(list(itertools.permutations(n)))
for i in arr:
    n1,com = func(n),func(i)
    if sorted(n) == list(sorted(i)) and n1 < com:
        ans = ""
        for j in i:
            ans += str(j)
        print(ans)
        exit()
print(0)
