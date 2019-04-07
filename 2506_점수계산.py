n = int(input())
point = [0 for i in range(n)]
temp = list(map(int,input().split()))
for i in range(len(point)):
    if temp[i] == 1:
        point[i] = point[i-1]+ 1
print(sum(point))
