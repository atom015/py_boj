for i in range(int(input())):
    n = list(map(int,input().split()))
    cnt = 0
    Average = sum(n[1:]) / n[0]
    for i in n[1:]:
        if i > Average:
            cnt += 1
    result = cnt / n[0]*100
    print(str("%.3f" % round(result,3) + '%'))

#이문제는 평균값이 소수점이면 내림을한다.
#틀렸던이유:
#1.두번째포문에 n리스트에 1번째인덱스부터 포문을돌렸어야했는데 그러지않았다
#2.print할때 str로 감싸지않았고 f포매팅외의round로 3번째 인덱스만출력하는 이중으로 하지않았다.
