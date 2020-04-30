s = input().split("-")
s[0] = sum(map(int,s[0].split("+")))

for i in range(1,len(s)):
    s[i] = -sum(map(int,s[i].split("+")))
print(sum(s))
#마이너스가 보이면 괄호시작 다음 마이너스 전까지
