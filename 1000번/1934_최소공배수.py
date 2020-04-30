#유클리드 호제법을 이용해서 풀어줬다.
#유클리드 호제법: 2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다.
for i in range(int(input())):
    a,b = list(map(int,input().split()))
    n1,n2 = a,b
    while True:
        if b != 0:
            r = a%b
            a = b
            b = r
        else:
            print(int(n1*n2/a))
            break
