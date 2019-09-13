a = [int(input()) for i in range(7)]
li = [i for i in a if i % 2 != 0]
if len(li) == 0:
    print(-1)
else:
    print(sum(li))
    print(min(li))
