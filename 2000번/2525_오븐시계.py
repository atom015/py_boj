A,B = map(int,input().split())
add = int(input())

if (B+add) > 59:
    A += (B+add) / 60
    B = (B + add) % 60
if A > 23:
    A %= 24
    B %= 60
elif (B+add) < 60:
    B += add
print('%d' % A,B)
