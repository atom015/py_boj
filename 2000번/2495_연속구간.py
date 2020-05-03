for i in range(3):
    s = input()
    ans,tmp,c = 0,1,s[0]
    for i in s[1:]:
        if i == c:
            tmp += 1
        else:
            c = i
            ans = max(ans,tmp)
            tmp = 1
    ans = max(ans,tmp)
    print(ans)
