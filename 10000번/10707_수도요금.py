a = int(input()) #X사의 1리터당 수도요금 A
b = int(input()) #Y사의 기본요금 B
c = int(input()) #Y사의 요금이 기본요금이 되는 사용량의 상한C가 입력된다.
d = int(input()) #Y사의 1리터당 추가요금 D
p = int(input()) #JOI군의 집에서 사용하는 한달간 수도양
xwt = 0
xwt += a*p
ywt = 0
if p <= c:
    ywt += b
else:
    ywt = p-c
    ywt = d*ywt
    ywt = b+ywt
if xwt < ywt:
    print(xwt)
else:
    print(ywt)
