import calendar
day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
a,b=map(int,input().split())

k = calendar.weekday(2007,a,b) #이함수는 월요일은 0 화요일은 1로 나타내주니까 day에 k인덱스를 출력해준다.

print(day[k])
