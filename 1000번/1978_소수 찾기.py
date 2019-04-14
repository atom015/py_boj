def prime_number(num):
    if num != 1: # 만약에 입력이 1이아니면
        for i in range(2,num): #2부터 num-1,ex)3까지 반복을 돈다
            if num % i == 0: #만약에 입력을 i로 나눈 나머지가 0이면 False를 리턴한다.
                return False
    else: #만약에 입력이 1이면 
        return False #False를 리턴 한다.
    
    return True #만약에 3개의 if문 하나라도 해당이안되면 True를 리턴한다.
cnt = 0
t = int(input())
n = list(map(int,input().split()))
for i in n:
    boolean = prime_number(i)
    if boolean == True:
        cnt += 1
print(cnt)