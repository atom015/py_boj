d = set()
b = set()
n,m = map(int,input().split())
for i in range(n):
    d.add(input())
for i in range(m):
    b.add(input())
result = sorted(list(d & b))
print(len(result))
for i in result:
    print(i)
