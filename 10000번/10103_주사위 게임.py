p1,p2 = 100,100
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    p2 = p2-a if a > b else p2
    p1 = p1-b if a < b else p1
print(p1)
print(p2)
