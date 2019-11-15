m,n = map(int,input().split())
def solution(m,n):
    a = [[0 for _ in range(n)] for _ in range(m)]
    i,j,num,chk,cnt = 0,-1,1,1,0
    while n > 0 and m > 0:
        for _ in range(n):
            j += chk
            a[i][j] = num
            num += 1
        m -= 1
        cnt += 1
        if m == 0 or n == 0:break
        for _ in range(m):
            i += chk
            a[i][j] = num
            num += 1
        n -= 1
        chk *= -1
        cnt += 1
    return cnt-1
print(solution(m,n))