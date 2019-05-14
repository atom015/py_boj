def main(li):
    n = [0 for i in range(5)]
    for i in range(5):
        n[i] = sum(li[i])
    winner = n.index(max(n))+1
    point = max(n)
    print(winner,point)
num = []
for i in range(5):
    num.append(list(map(int,input().split())))
main(num)