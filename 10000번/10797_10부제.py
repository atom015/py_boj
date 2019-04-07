temp = 0
day = int(input())
car_number = list(map(int,input().split()))
for i in range(len(car_number)):
    if day == car_number[i]:
        temp += 1
print(temp)
