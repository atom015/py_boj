def le(li,n):
    tmp1 = [[] for i in range(n)]
    tmp2 = []
    for i in range(n):
        for j in range(n):
            tmp1[j].append(li[i][j])
    for i in range(n):
        tmp2.append("".join(tmp1[i]))
    return tmp2
def main():
    n = int(input())
    w,l = 0,0
    width = []
    for i in range(n):
        width.append(input())
    length = le(width,n)
    for i in range(n):
        wc,lc = 0,0
        for j in range(n):
            if width[i][j] == ".":
                wc += 1
            else:
                wc = 0
            if wc == 2:
                w += 1
            if length[i][j] == ".":
                lc += 1
            else:
                lc = 0
            if lc == 2:
                l += 1
    print(w,l)

main()
