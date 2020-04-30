def main(li):
    Remainder = set()
    for i in li:
        Remainder.add(i%42)
    return len(Remainder)
li = []
for i in range(10):
    li.append(int(input()))
print(main(li))
