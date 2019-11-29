for i in range(int(input())):
    a,b = input().split()
    a,mod = int(a),0
    for j in b:
        mod += int(j,a) % (a-1)
    print(mod % (a-1))
