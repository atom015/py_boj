n,b,h,w = map(int,input().split()) #참가자수,예산,호텔의수,고를수있는주의개수
cost = [] #비용
ps = [] #인원
min,sum = b+1,0
for i in range(h):
    cost.append(int(input()))
    ps.append(list(map(int,input().split())))
for i in range(h):
    for j in range(w):
        if ps[i][j] >= n:
            sum = cost[i]*n
    if min > sum and sum != 0:
        min = sum
if min <= b:
    print(min)
else:
    print("stay home")
