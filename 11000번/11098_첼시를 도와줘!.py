for i in range(int(input())):
    arr = []
    for j in range(int(input())):
        a,b = input().split()
        arr.append([int(a),b])
    arr.sort()
    print(arr[-1][1])
