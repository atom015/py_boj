n = int(input()) #과목의 개수
li = list(map(int,input().split())) #현재성적
s = [i/max(li)*100 for i in li] #고친성적으로 점수/m(최대값)*100으로 고쳐준다.
print(sum(s)/len(li)) #모든점수/과목의개수로 평균을 구해서 출력해준다.
