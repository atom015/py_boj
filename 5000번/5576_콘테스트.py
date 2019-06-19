w = [int(input()) for i in range(10)]
k = [int(input()) for i in range(10)]
wsum = 0
ksum = 0
for i in range(3):
    wsum += max(w)
    ksum += max(k)
    w.remove(max(w))
    k.remove(max(k))
print(wsum,ksum)
