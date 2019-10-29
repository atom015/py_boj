arr = [[0,0,0,0,1],[0,0,0,0,2],[0,0,0,0,3]]
for i in range(int(input())):
    a,b,c = map(int,input().split())
    arr[0][a] += 1
    arr[1][b] += 1
    arr[2][c] += 1
    arr[0][0] += a
    arr[1][0] += b
    arr[2][0] += c
arr.sort(key=lambda t:(-t[0],-t[1],-t[2],-t[3]))
if arr[0][0:4] == arr[1][0:4]:
    print(0,arr[0][0])
else:
    print(arr[0][4],arr[0][0])
