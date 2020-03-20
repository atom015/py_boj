a,b,c = map(int,input().split())
print(-1 if b >= c else int((-(a/(b-c))+1)))
