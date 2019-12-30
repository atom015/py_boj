a1,p = map(int,input().split())
d = []
def func(a):
    if (a in d) == True:
        d.append(a)
        return
    d.append(a)
    num = 0
    a = str(a)[::-1]
    for i in range(len(str(a))):
        num += int(a[i])**p
    func(num)
func(a1)
delete = d.pop()
del d[d.index(delete):]
print(len(d))
