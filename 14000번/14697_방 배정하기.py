import sys
a,b,c,d = map(int,input().split())
for i in range(50):
    for ii in range(50):
        for j in range(50):
            if (i*a+ii*b+j*c) == d: #(i*a(방의정원))+(ii*b(방의정원))+(j*c(방의정원)) == d(전체 학생수)
                print(1)
                sys.exit()
print(0)
sys.exit()
#브루트포스
