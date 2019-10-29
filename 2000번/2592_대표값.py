a = [int(input()) for i in range(10)]
print(sum(a)//len(a))
def func():
    dic = {i:0 for i in a}
    for i in a:
        dic[i] += 1
    for k,v in dic.items():
        if v == max(dic.values()):
            return k
print(func())
