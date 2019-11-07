joi,ioi = 0,0
n = input()
for i in range(len(n)):
    if i <= len(n)-3:
        if n[i:i+3] == "JOI":
            joi += 1
        if n[i:i+3] == "IOI":
            ioi += 1
print(joi)
print(ioi)