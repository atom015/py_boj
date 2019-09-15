"""
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

예제 입력 1
4
1 3 5 7
예제 출력 1
3
"""
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
    if prime_number(i) == True: #만약에 소수면 cnt에 1을더해준다.
        cnt += 1
print(cnt)
