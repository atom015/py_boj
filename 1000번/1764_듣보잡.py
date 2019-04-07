d = []
b = []
n,m = map(int,input().split())
for i in range(n):
    d.append(input())

for i in range(m):
    b.append(input())

d1 = set(d)
b1 = set(b)
result = d1 & b1
result = sorted(list(result))
print(len(result))
for i in result:
    print(i)
