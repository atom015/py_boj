d = set()
b = set()
n,m = map(int,input().split()) #n,m을 입력받는다.
for i in range(n): #듣도못한사람
    d.add(input())
for i in range(m): #보도못한사람
    b.add(input())
result = sorted(list(d & b)) #서로 겹치는 듣보잡을 구한다음에 리스트로 바꾼후 사전순으로 정렬한다.
print(len(result)) #길이출력
for i in result: #출력
    print(i)
