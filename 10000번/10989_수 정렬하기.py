import sys
arr = [0 for i in range(10000)]
for i in range(int(input())):
    arr[int(sys.stdin.readline())-1] += 1
for i,c in enumerate(arr):
    if c > 0:
        print(c*"{}\n".format(i+1),end='')
