a = [1,2,3,4,5,6,7,8]
n = list(map(int,input().split()))
if a == n:
    print("ascending")
elif a[::-1] == n:
    print("descending")
else:
    print("mixed")
