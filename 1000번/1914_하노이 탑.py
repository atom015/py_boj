ans = []
n = int(input())
if n < 21:
    def hanoi(num,A,B,C):
        if num == 1:
            ans.append([A,C])
        else:
            hanoi(num-1,A,C,B)
            ans.append([A,C])
            hanoi(num-1,B,A,C)
    hanoi(n,1,2,3)
    print(len(ans))
    for i in ans:
        print(*i)
else:
    print(2**n-1)
