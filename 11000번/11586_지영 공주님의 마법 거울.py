def one():
    for i in range(n):
        print(arr[i])
def two():
    for i in range(n):
        print(arr[i][::-1])
def three():
    for i in reversed(arr):
        print(i)
n = int(input())
arr = [input() for i in range(n)]
k = int(input())
if k == 1:
    one()
elif k == 2:
    two()
else:
    three()
