n,m = map(int,input().split())
arr = []
s1 = [".","O","-","|","/","\\","^","<","v",">"]
s2 = [".","O","|","-","\\","/","<","v",">","^"]
for i in range(n):
    arr.append(list(input()))
i,j = 0,m-1
while 1:
    for k in range(10):
        if ord(arr[i][j]) == 92:
            print("/",end='')
            break
        elif ord(arr[i][j]) == 47:
            print("\\",end='')
            break
        elif arr[i][j] == s1[k]:
            print(s2[k],end='')
            break
    if j == 0 and i == n-1:
        break
    if i == n-1:
        i = 0
        j -= 1
        print()
    else:
        i += 1
