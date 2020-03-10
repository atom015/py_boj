a,b = map(int,input().split())
print(a//b,end='.')
tmp = a%b
for i in range(1000):
    tmp *= 10
    if tmp == 0:break
    print(tmp//b,end='')
    tmp %= b
  
