T = [i*(i+1)//2 for i in range(1,46)]
def func(n):
    for i in T:
        for j in T:
            for k in T:
                if i+j+k == n:
                    return 1
    return 0

for i in range(int(input())):
    n = int(input())
    print(func(n))
