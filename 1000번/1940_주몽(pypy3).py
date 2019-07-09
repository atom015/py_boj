n = int(input()) #재료의 개수
m = int(input()) #갑옷을 만드는 숫자의 개수
li = list(map(int,input().split())) #재료가 가진 개수
cnt = 0
for i in range(n): #for문을 n번돈다.
    for j in range(i+1,n): #중복없이 i+1부터 n까지 반복한다.
        if (li[i] + li[j]) == m: #만약에 두값을더한게 필요한 재료숫자랑같다면
            cnt += 1 #cnt에 1을 더해준다.
print(cnt)
#원래는 python으로 풀어야했으나 시간초과 때문에;;;
