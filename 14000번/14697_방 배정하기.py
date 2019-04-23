import sys
a,b,c,d = map(int,input().split())
for i in range(50):
    for ii in range(50):
        for j in range(50):
            if (i*a+ii*b+j*c) == d:
                print(1)
                sys.exit()
print(0)
sys.exit()