class position:
    def __init__(self,x,y):
        self.x = x
        self.y = y
p = []
for i in range(3):
    a,b = map(int,input().split())
    p.append(position(a,b))
f = (p[1].x-p[0].x)*(p[2].y-p[0].y)
s = (p[1].y-p[0].y)*(p[2].x-p[0].x)
ret = f-s
print(-1 if 0 > ret else (1 if 0 < ret else 0))
