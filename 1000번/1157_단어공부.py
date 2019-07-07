n = input().upper() #대소문자는 구분하지않으니까 대문자로 바꾸어주었다.
chk = {i:0 for i in set(n)} #각각 단어들만 넣어주었다 (값은 0으로)
for i in n: #n을 돌면서 단어들개수를 더해준다.
    chk[i] += 1
max = max(chk.values()) #가장 많은단어개수
result = set(k for k,v in chk.items() if max == v) #중복없이 max랑 값이 같은것들을 넣어준다.
if len(result) == 1: #만약에 단어가 한개면 그단어 출력
    print(result.pop())
else: #아니면 "?"출력
    print("?")
