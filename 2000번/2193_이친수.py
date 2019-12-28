def main():
    n = int(input())
    if n <= 2:
        return 1
    d = [0 for i in range(n)]
    d[0] = 1
    d[1] = 1
    for i in range(2,n):
        d[i] = d[i-1]+d[i-2]
    return d[n-1]
print(main())
