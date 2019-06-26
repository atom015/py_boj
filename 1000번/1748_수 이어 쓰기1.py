n = int(input())
result,i = 0,1
while i <= n:
    result += (n-i+1)
    i *= 10
print(result)
