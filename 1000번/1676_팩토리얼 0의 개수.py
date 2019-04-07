n = int(input())
def Factorial(f):
    mul = 1
    cnt = 0
    for i in range(1,f+1):
        mul *= i
    div = str(mul)[::-1]
    for i in div:
        if i != "0":
            break
        else:
            cnt += 1
    return cnt
print(Factorial(n))
