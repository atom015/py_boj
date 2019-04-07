a = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}
n = [-1 for i in range(26)]
s = list(input())

for i in range(len(n)):
    for j in range(len(s)):
        temp = s[j]
        if temp == a[i]:
            n[i] = s.index(temp)

for i in range(len(n)):
    print(n[i],end=' ')
"답 : 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1"
