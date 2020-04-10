def func(n):
    li = []
    for i in range(2,n+1):
        while n % i == 0:
            li.append(i)
            n //= i
    return li
for i in range(int(input())):
    n = int(input())
    ans = func(n)
    s = sorted(list(set(ans)))
    for i in s:
        print(i,ans.count(i))
