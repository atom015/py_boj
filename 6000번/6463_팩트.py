from math import factorial
compare = 0
result = {}
while 1:
    try:
        n = int(input())
        if compare < len(str(n)):
            compare = len(str(n))
        li = list(str(factorial(n)))[::-1]
        for i in li:
            if "0" != i:
                ans = i
                break
        result["{} -> {}".format(n,ans)] = len(str(n))
    except :
        break

for k,v in result.items():
    print(" "*(compare-v)+"",k)
