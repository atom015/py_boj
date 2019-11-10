dic = ["N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M"]
n = list(input())
for i in range(len(n)):
    if n[i] == " " or n[i].isdigit():
        continue
    elif n[i].islower():
        n[i] = dic[ord(n[i].upper())-ord("A")].lower()
    else:
        n[i] = dic[ord(n[i])-ord("A")]
print("".join(n))
