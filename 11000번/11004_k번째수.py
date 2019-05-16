def main(li,k):
    return li[k-1]

n,k = map(int,input().split())
An = sorted(list(map(int,input().split())))
print(main(An,k))