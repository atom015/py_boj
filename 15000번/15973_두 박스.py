x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())
if (x1,y1) == (x4,y4) or (x2,y2) == (x3,y3) or (x2,y1) == (x3,y4) or (x1,y2) == (x4,y3):
    print("POINT")
elif x1 > x4 or x2 < x3 or y1 > y4 or y2 < y3:
    print("NULL")
elif x2 == x3 or x1 == x4 or y2 == y3 or y1 == y4:
    print("LINE")
else:
    print("FACE")
