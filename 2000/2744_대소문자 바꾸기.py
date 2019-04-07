n = list(input())
for i in range(len(n)):
    if n[i].islower() == True:
        n[i] = n[i].upper()
    elif n[i].isupper() == True:
        n[i] = n[i].lower()
for i in n:
    print(i,end='')
