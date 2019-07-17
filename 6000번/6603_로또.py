import itertools
while 1:
    li = list(map(int,input().split()))
    k = li.pop(0)
    if k == 0:
        break
    result = list(itertools.combinations(li,6))
    for i in range(len(result)):
        for j in range(6):
            print(result[i][j],end=' ')
        print()
    print()
