def func(n):
    c = True if len(str(n)) <= 2 else False #삼항연산자(참인경우 값 if 조건 else 거짓인경우 값)
    li = []
    chk = False
    if c == True:
        return True
    a = list(str(n))
    for i in range(len(a)):
        if i != len(a)-1:
            li.append(int(a[i+1])-int(a[i]))
    for i in range(len(li)):
        if i != len(li)-1:
            if li[i-1] == li[i]:
                chk = True
            else:
                chk = False
    if chk == False:
        return False
    else:
        return True

cnt = 0
n = int(input())
for i in range(1,n+1):
    if func(i) == True:
        cnt += 1
print(cnt)
#차이를 다음인덱스-현재인덱스로 구한다음
