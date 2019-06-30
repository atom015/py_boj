from math import sqrt
def is_int(n):
    if int(n) == n:
        return True
    return False
result = []
n = int(input())
m = int(input())
for i in range(n,m+1):
    if is_int(sqrt(i)) == True:
        result.append(i)
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
