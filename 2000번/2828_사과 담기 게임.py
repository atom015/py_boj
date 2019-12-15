n,m = map(int,input().split())
J = int(input())
s,e,ret = 1,m,0
for i in range(J):
    apple = int(input())
    if s <= apple <= e:
        continue
    if e < apple:
        ret += apple-e
        s += apple-e
        e = apple
    else:
        ret += s-apple
        e -= s-apple
        s = apple
print(ret)
