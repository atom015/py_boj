n = int(input())
li = list(map(int,input().split()))
s = [i/max(li)*100 for i in li]
print(sum(s)/len(li))
