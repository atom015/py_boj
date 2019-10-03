dic = {}
a = []
for i in range(int(input())):
    n,d,m,y = input().split()
    a.append([int(y),int(m),int(d)])
    dic[n] = [int(y),int(m),int(d)]
MAX,MIN = max(a),min(a)
for k,v in dic.items():
    if v == MAX:
        MAX = k
    if v == MIN:
        MIN = k
print(MAX)
print(MIN)
