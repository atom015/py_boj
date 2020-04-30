n,m = map(int,input().split())
n1,m2 = n,m
while 1:
    if m != 0:
        r = n%m #a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다
        n = m
        m = r
    else:
        print(n)
        print(int(n1*m2/n)) #n*m = L*G라는 성질을이용
        break
