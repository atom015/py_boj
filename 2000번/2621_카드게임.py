
color = []
nums = []
ans = 0
for i in range(5):
    a,b = input().split()
    color.append(a)
    nums.append(int(b))
def checking1(arr):
    arr.sort()
    t = abs(arr[1]-arr[0])
    for i in range(1,5):
        if i+1 < 5:
            if arr[i]+t != arr[i+1]:
                return False
    return True
def same_chk(arr):
    for i in arr:
        if arr.count(i) == 4:
            return i
    return False
def checking2(arr):
    arr.sort()
    chk = [0,0]
    for i in arr:
        if arr.count(i) == 3:
            chk[0] = i
        if arr.count(i) == 2:
            chk[1] = i
    if all(chk):
        return [chk[0],chk[1]]
    return False
def checking3(arr):
    for i in arr:
        if arr.count(i) == 3:
            return i
    return False
def checking5(arr):
    chk = [0,0]
    s = set(arr)
    ix = 0
    for i in s:
        if arr.count(i) == 2:
            chk[ix] = i
            ix += 1
    if all(chk):
        return sorted(chk)
    return False
def checking6(arr):
    for i in arr:
        if arr.count(i) == 2:
            return i
    return False
#1번째 규칙
if color[0] == color[1] == color[2] == color[3] == color[4] and checking1(nums):
    print(max(nums)+900)
    exit()
#2번째 규칙
tmp = same_chk(nums)
if tmp:
    print(tmp+800)
    exit()
#3번째 규칙
tmp = checking2(nums)
if tmp != False:
    print(tmp[0]*10+tmp[1]+700)
    exit()
#4번째 규칙
if color[0] == color[1] == color[2] == color[3] == color[4]:
    print(max(nums)+600)
    exit()
#5번째 규칙
if checking1(nums):
    print(max(nums)+500)
    exit()
#6번째 규칙
tmp = checking3(nums)
if tmp:
    print(tmp+400)
    exit()
#7번째 규칙
tmp = checking5(nums)
if tmp:
    print(max(tmp)*10+min(tmp)+300)
    exit()
#8번째 규칙
tmp = checking6(nums)
if tmp != False:
    print(tmp+200)
    exit()
#9번째 규칙
print(max(nums)+100)
