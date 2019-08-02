n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
a.sort(key=lambda x : (x[1], x[0]))
s = [a[0]]
j = 0
for i in range(1,n):
    if a[i][0] >= a[j][1]:
        s += [a[i]]
        j = i
print(len(s))
#시간들을 끝나는 순서대로 정렬한후에 첫번째회의를 리스트에 넣고 첫번째 회의를 기준으로
#잡고 회의 시간이 겹치지 않으면 리스트에 넣어준다. 회의수를 세기위해 길이를 print해준다.
#겹치지않을려면 기준으로 잡은회의에 끝나는시간이 비교할회의시간의 시작시간보다 작아야한다.
