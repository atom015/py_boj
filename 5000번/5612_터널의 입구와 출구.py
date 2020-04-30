n = int(input())
m = int(input())
temp = m
result = m
for i in range(n):
    push,pop = map(int,input().split())
    temp += push-pop
    if temp < 0:
        print(0)
        exit()
    result = max(result,temp)
print(result)
