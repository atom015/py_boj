n = int(input())
m = int(input())
li = list(map(int,input().split()))
cnt = 0
chk = []
for i in range(n):
    for j in range(n):
        if i != j:
            if li[i]+li[j] == m and li[i] not in chk and li[j] not in chk:
                chk.append(li[i])
                chk.append(li[j])
                cnt += 1
print(cnt)
