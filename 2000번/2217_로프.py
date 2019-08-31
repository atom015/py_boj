n = int(input())
a = [int(input()) for i in range(n)]
def main(n):
    a.sort(reverse=True)
    if n == 1:
        return a[0]
    if n == 2:
        return min(a)*len(a)
    else:
        compare = []
        c = 0
        for i in range(n):
            if i == 0:
                compare.append(a[i])
                c = a[i]
            else:
                compare.append(a[i])
                tmp = a[i]*len(compare)
                if c < tmp:
                    c = tmp
        return c
print(main(n))
