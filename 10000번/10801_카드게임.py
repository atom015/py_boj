a = list(map(int,input().split()))
a_cnt = 0
b = list(map(int,input().split()))
b_cnt = 0
for i in range(10):
    if a[i] > b[i]:
        a_cnt += 1
    elif a[i] < b[i]:
        b_cnt += 1
if a_cnt == b_cnt:
    print("D")
elif a_cnt > b_cnt:
    print("A")
elif a_cnt < b_cnt:
    print("B")