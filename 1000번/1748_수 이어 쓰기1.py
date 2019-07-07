n = int(input())
result,i = 0,1
#수이어쓰기 식
while i <= n:
    result += (n-i+1)
    i *= 10
print(result)
