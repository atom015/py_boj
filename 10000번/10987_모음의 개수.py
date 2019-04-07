result = 0
mo = ["a","e","i","o","u"]
n = list(input())
for i in n:
    for j in mo:
        if i == j:
            result += 1
print(result)
