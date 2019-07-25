n = int(input())
li = list(map(int,input().split()))
sd = set() #증가수열 중복없애주는 set
result = [] #오르막길의 크기를 저장하는 리스트
#minus함수는 리스트가 [1,3,5,6,7] 이런식으로 있으면 큰수에서 작은수를 빼기위해 sort하고 뒤집어줬다.
#[7,6,5,3,1]이렇게 있으면 7-6,6-5,5-3,3-1이런식으로 빼주도록 만들었다.
def minus(l): #l = 증가수열
    l.sort(reverse=True)
    m = 0
    for i in range(len(l)):
        if i != len(l)-1:
            m += l[i]-l[i+1]
    return m
for i in range(n):
    if i >= 1: #i-1을 하기위해 "i가 1보다 크면?"이라는 if를 달아줬다.
        c = li[i-1] #비교변수
        if c < li[i]: #만약에 i-1값이 i값보다작으면
            #sd에 비교변수와 i번째값을 넣어준다. 이때 li[i-1]이랑 c랑같으니까 중복되면 안되니까 set에 추가해준다.
            sd.add(c)
            sd.add(li[i])
            continue
        #증가수열이 끝났으면 minus함수에 sd 세트를 리스트로 바꿔서 오르막길 값을 result에 넣어준다.
        result.append(minus(list(sd)))
        sd = set() #set값 초기화
#혹시나 set안에 값이 남아있을수도 있으니 minus로 한번더 돌려준다.
result.append(minus(list(sd)))
#만약에 오르막길이 없으면 0출력 있으면가장큰값 출력
if len(result) == 0:
    print(0)
else:
    print(max(result))
#증가수열
