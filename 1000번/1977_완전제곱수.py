from math import sqrt
def is_int(n):
    if int(n) == n: #정수인지검색
        return True #정수면 True
    return False #아니면 False를 return한다.
result = []
n = int(input())
m = int(input())
for i in range(n,m+1): #n부터 m+1까지 반복하면서
    if is_int(sqrt(i)) == True: #만약에 완전제곱수면
        result.append(i) #result에 추가해준다.
if len(result) == 0: #만약에 완전제곱수가 없으면
    print(-1) #-1출력
else: #만약에 완전제곱수가 있으면
    print(sum(result)) #더한값과
    print(min(result)) #제일 작은값출력
