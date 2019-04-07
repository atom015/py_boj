from collections import Counter
self_num = {}
tn = []
for i in range(1,10001):
    if len(str(i)) >= 2:
        tmp = list(str(i))
        int_list = [int(i) for i in tmp]
        self_num[i] = sum(int_list)+i
    else:
        self_num[i] = i+i
for k,v in self_num.items():
    tn.append(k)
    tn.append(v)
chk = Counter(tn)
for i in chk.keys():
    if chk[i] == 1:
        if i >= 10000:
            continue
        print(i)
