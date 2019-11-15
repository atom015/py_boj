ret = 0
for i in range(int(input())):
    a,b = map(int,input().split())
    ret += b%a
print(ret)