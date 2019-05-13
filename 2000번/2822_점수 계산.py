def main(li):
    result = 0
    num = []
    for _ in range(5):
        result += max(li)
        num.append(li.index(max(li))+1)
        li[li.index(max(li))] = 0
    print(result)
    for i in sorted(num):
        print(i,end=' ')
num_li = []
for i in range(8):
    num_li.append(int(input()))
main(num_li)