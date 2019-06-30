li = ["c=","c-","dz=","d-","lj","nj","s=","z="]
a = input()

for i in li:
    a = a.replace(i,"*")
print(len(a))
