def chk(a):
    a = [int(i) for i in a]
    li = []
    chk = False
    if len(a) <= 2:
        return True
    for i in range(len(a)):
        if i != len(a)-1:
            li.append(a[i+1]-a[i])
    for i in range(len(li)):
        if i != len(li)-1:
            if li[i] == li[i+1]:
                chk = True
            else:
                return False
    if chk == True:
        return True
if chk(list(input())) == True:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    print("흥칫뿡!! <(￣ ﹌ ￣)>")
