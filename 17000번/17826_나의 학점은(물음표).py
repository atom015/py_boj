a = list(map(int,input().split()))
point = int(input())
rank = a.index(point)+1
ans = ""
ans = "A+" if 1 <= rank <= 5 else ans
ans = "A0" if 6 <= rank <= 15 else ans
ans = "B+" if 16 <= rank <= 30 else ans
ans = "B0" if 31 <= rank <= 35 else ans
ans = "C+" if 36 <= rank <= 45 else ans
ans = "C0" if 46 <= rank <= 48 else ans
ans = "F" if 49 <= rank <= 50 else ans
print(ans)
