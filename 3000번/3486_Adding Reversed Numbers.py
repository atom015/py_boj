for i in range(int(input())):
    n,m = input().split()
    sum = str(int(n[::-1])+int(m[::-1]))[::-1]
    print(int(sum))
