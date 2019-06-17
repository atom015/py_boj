man = list(map(int,input().split()))
min = list(map(int,input().split()))
if sum(man) < sum(min):
    print(sum(min))
elif sum(man) > sum(min):
    print(sum(man))
else:
    print(sum(min))
