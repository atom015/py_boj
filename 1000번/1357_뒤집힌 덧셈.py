x,y = input().split() #string형태로 값 두개를 받는다.
result = int(x[::-1])+int(y[::-1]) #두값을 뒤집고 int로 바꿔준다음 두값을 더해줬다.
print(int(str(result)[::-1])) #그다음 뒤집어서 int로 바꾸어주었다.
