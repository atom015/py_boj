from datetime import *
M,D = map(int,input().split())
print(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][datetime(2009,D,M).weekday()])
