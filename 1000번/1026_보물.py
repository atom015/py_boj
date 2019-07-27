n = int(input())
a = list(map(int,input().split()))
b = sorted(list(map(int,input().split())))
a.sort(reverse=True)
s = 0
for i in range(n):
    s += a[i]*b[i]
print(s)
#최소값을 구해야하니까 a는 오름차순 b는 내림차순으로 정렬한다.
#그래서 각항을 곱한다.
