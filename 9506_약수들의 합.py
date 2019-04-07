while True:
    num = int(input())
    if num == -1:
        break
    y = []
    for i in range(1,num+1):
        if i == num:
            break
        if num%i == 0:
            y.append(i)
    if sum(y) == num:
        y = [str(i) for i in y]
        st = " + ".join(y)
        print("{} = {}".format(num,st))
    else:
        print(num,"is NOT perfect.")
