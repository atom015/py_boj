s = input()
arr = {}
for i in range(int(input())):
    n = input()
    l,o,v,e = s.count("L")+n.count("L"),s.count("O")+n.count("O"),s.count("V")+n.count("V"),s.count("E")+n.count("E")
    arr[n] = (((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e)) % 100)
ans = []
for k,v in arr.items():
    if v == max(arr.values()):
        ans.append(k)
print(sorted(ans)[0])
