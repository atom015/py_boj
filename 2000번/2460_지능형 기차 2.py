arr = []
s = 0
for i in range(10):
    a,b = map(int,input().split())
    s -= a
    s += b
    arr.append(s)
print(max(arr))
