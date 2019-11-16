n,m = map(int,input().split()) #가로 세로
k = int(input())
if n*m < k:
    print(0)
    exit()
a = [[0 for _ in range(n)] for _ in range(m)]
def snail(n,m):
    i,j,num,idx = n,0,1,0
    d = [-1,1,1,-1]*(m+1)
    chk = d[idx]
    while n > 0:
        ### 세로 ##
        for _ in range(n):
            i += chk
            a[i][j] = num
            num += 1
        m -= 1
        if m == 0:break
        ### 방향 ###
        chk = d[idx+1]
        idx += 1
        ### 가로 ###
        for _ in range(m):
            j += chk
            a[i][j] = num
            num += 1

        n -= 1
        chk = d[idx+1]
        idx += 1

snail(m,n)
def main():
    for i in range(m):
        for j in range(n):
            if a[i][j] == k:
                if m-(i+1) == 0:
                    print(j+1,1)
                    return
                else:
                    print(j+1,m-(i+1)+1)
                    return
main()
