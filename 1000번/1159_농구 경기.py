li = [input() for i in range(int(input()))]#입력받은수만큼 리스트에 입력받은 단어들을 넣어준다.
overlap = set(i[0] for i in li)#중복없이 첫글자를 넣어준다.
chk = {i:0 for i in overlap} #첫글자를 값을 0으로해서 딕셔너리에 넣어준다.
for i in li: #단어들 개수체크
    chk[i[0]] += 1
result = [k for k,v in chk.items() if v >= 5] #만약에 첫글자 같은사람이 5명이상이면 result에 넣어준다.
if len(result) == 0: #만약에 첫글자가 같은사람이 5명을 넘지않으면
    print("PREDAJA") #"PREDAJA"출력
else:#넘으면
    for i in sorted(result): #사전순으로 출력
        print(i,end='')
