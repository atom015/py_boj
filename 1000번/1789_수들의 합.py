n = int(input()) #자연수 s를 받는다.
sum = 0
num = 1 #수를 더할땐 1부터 더해야하니까 1부터시작
while 1: #while을 돈다.
    sum += num #증가하는수를 sum에더해준다.
    if sum > n: #만약에 n이 sum보다 작다면
        print(num-1) #num-1출력
        break
    num += 1 #1부터 증가
