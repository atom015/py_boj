a,b,c = map(int,input().split())
plus = int(input())
c += plus
b += c//60
c %= 60
a += b//60
b %= 60
a %= 24
print(a,b,c)
