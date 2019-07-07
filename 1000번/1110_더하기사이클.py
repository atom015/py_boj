cnt = 0 #사이클의 길이체크
n = input() #ex)26
c = [int(i) for i in n] #입력받은수를 정수리스트로 나눈다 ,ex)[2,6]
c = str(c[-1])+str(sum(c))[-1] #ex)"6"+"8"
#이런식으로 다시 원래수로 돌아올때까지 반복한다.
while 1:
    cnt += 1
    if int(c) == int(n):
        break
    c = [int(i) for i in c]
    c = str(c[-1])+str(sum(c))[-1]
print(cnt) #사이클길이 출력
