"""
문제:
어떤 양의 정수 X의 자리수가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

예제 입력 1
110
예제 출력 1
99
예제 입력 2
1
예제 출력 2
1
예제 입력 3
210
예제 출력 3
105
예제 입력 4
1000
예제 출력 4
144
"""
def func(n):
    c = True if len(str(n)) <= 2 else False #삼항연산자(참인경우 값 if 조건 else 거짓인경우 값)
    li = []
    chk = False
    if c == True:
        return True
    a = list(str(n))
    for i in range(len(a)):
        if i != len(a)-1:
            li.append(int(a[i+1])-int(a[i]))
    for i in range(len(li)):
        if i != len(li)-1:
            if li[i-1] == li[i]:
                chk = True
            else:
                chk = False
    if chk == False:
        return False
    else:
        return True

cnt = 0
n = int(input())
for i in range(1,n+1):
    if func(i) == True:
        cnt += 1
print(cnt)
#차이를 다음인덱스-현재인덱스로 구한다음 만약 차이가 모두 같다면 True출력 아니면 False출력
