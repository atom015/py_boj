def FIB(n):
    cnt = 1
    fib = [0, 1]
    for i in range(fib[1], n):
        sum = fib[i-1] + fib[i]
        fib.append(sum)
    return fib[len(fib)-1]
n = int(input())
print(FIB(n))