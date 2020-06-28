month = int(input())
day = int(input())
if 2 < month or (2 == month and 18 < day):
    print("After")
elif 2 == month and 18 == day:
    print("Special")
else:
    print("Before")
