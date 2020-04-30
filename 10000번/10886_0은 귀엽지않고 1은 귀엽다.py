zero = 0
one = 0
for i in range(int(input())):
    a = int(input())
    if a == 1:
        one += 1
    elif a == 0:
        zero += 1
if one > zero:
    print("Junhee is cute!")
elif one < zero:
    print("Junhee is not cute!")
