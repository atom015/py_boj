n = int(input())
s = 0
for i in range(n):
    s += sum(list(map(int,input().split())))
print(s)
