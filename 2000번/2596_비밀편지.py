N = int(input())
s = input()
ans = []

# A~H까지의 문자열
Al = ["A","B","C","D","E","F","G","H"]
al = ["000000","001111","010011","011100","100110","101001","110101","111010"]

# 중복체크
def checking(s):
    tmp = -1
    for i in range(8):
        cnt = 0
        for j in range(6):
            if s[j] != al[i][j]:
                cnt += 1
        if cnt == 0:
            return i
        if cnt == 1:
            tmp = i
    return tmp
# 6칸씩 나누기
cnt = 0
for i in range(6,N*6+1,6):
    tmp = checking(s[i-6:i])
    if tmp == -1:
        print(cnt+1)
        exit()
    else:
        ans.append(tmp)
    cnt += 1
for i in ans:print(Al[i],end='')
