for i in range(int(input())):
    n = list(map(int,input().split()))
    cnt = 0
    Average = sum(n[1:]) / n[0]
    for i in n[1:]:
        if i > Average:
            cnt += 1
    result = cnt / n[0]*100
    print(str("%.3f" % round(result,3) + '%'))
