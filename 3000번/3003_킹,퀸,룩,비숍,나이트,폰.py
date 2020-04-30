compare = [1,1,2,2,2,8] #비교 리스트
a = list(map(int,input().split()))
for i in range(len(compare)):
    print(compare[i]-a[i],end=' ')
