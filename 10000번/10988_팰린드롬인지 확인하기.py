p = list(input())
for i in range(len(p)):
    t = p[::-1]
    p = ''.join(p)
    t = ''.join(t)
if p == t:
    print("1")
else:
    print("0")
