N = int(input())
happy = list(map(int,input().split()))
high = max(happy)
low = min(happy)
temp = high - low
print(temp)
