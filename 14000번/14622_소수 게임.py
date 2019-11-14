import sys
ip = sys.stdin.readline
def so(n):
    if n == 1:return False
    i = 2
    while i*i <= n:
        if n % i == 0:return False
        i += 1
    return True
a,b = [],[]
chk = [False for i in range(5000001)]
def main():
    p1,p2 = 0,0 # 대웅 규성
    for i in range(int(ip())):
        n,m = map(int,ip().split())
        if so(n):
            if chk[n]: p1 -= 1000
            else:
                a.append(n)
                a.sort()
                chk[n] = True
        else:
            if len(b) < 3:p2 += 1000
            else:p2 += b[-3]
        if so(m):
            if chk[m]:p2 -= 1000
            else:
                b.append(m)
                b.sort()
                chk[m] = True
        else:
            if len(a) < 3:p1 += 1000
            else: p1 += a[-3]

    if p1 < p2:
        return "소수 마스터 갓규성"
    elif p1 > p2:
        return "소수의 신 갓대웅"
    else:
        return "우열을 가릴 수 없음"
print(main())
