m = int(input())
n = int(input())
cnt = []
def prime(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True
for i in range(m,n+1):
    if prime(i) == True:
        cnt.append(i)
if len(cnt) == 0:
    print(-1)
else:
    cnt = sorted(cnt)
    print(sum(cnt))
    print(min(cnt))
