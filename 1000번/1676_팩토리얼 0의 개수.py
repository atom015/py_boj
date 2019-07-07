n = int(input()) #n을 입력받는다
def Factorial(f):
    mul = 1 #팩토리얼을 구하기위해 1부터 시작해준다.
    cnt = 0 #
    #팩토리얼을 구하는 for문
    for i in range(1,f+1):
        mul *= i
    div = str(mul)[::-1] #팩토리얼을 뒤집어서 뒤에서 부터 시작한다.
    for i in div:
        if i != "0": #뒤에서부터 돌면서 0이아닌숫자가 나오면 끝낸다.
            break
        else: #아니면 0의개수를 새준다.
            cnt += 1
    return cnt
print(Factorial(n)) #출력
