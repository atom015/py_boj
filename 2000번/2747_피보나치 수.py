n = int(input())
cnt = 1
fib = [0, 1]
for i in range(fib[1], n):
    sum = fib[i-1] + fib[i]
    fib.append(sum)
print(fib[len(fib)-1])