li = [list(input()) for i in range(8)] #8*8칸으로 만들어주기위해서 이런식으로 만들어주었다.
cnt = 0 #말들을 체크하기위해
#하얀칸이있는 인덱스를 넣어주었다.
location = [[0,0],[0,2],[0,4],[0,6],
            [1,1],[1,3],[1,5],[1,7],
            [2,0],[2,2],[2,4],[2,6],
            [3,1],[3,3],[3,5],[3,7],
            [4,0],[4,2],[4,4],[4,6],
            [5,1],[5,3],[5,5],[5,7],
            [6,0],[6,2],[6,4],[6,6],
            [7,1],[7,3],[7,5],[7,7]]
for i in range(len(location)): #하얀칸이있는 리스트를 돈다.
    if li[location[i][0]][location[i][1]] == "F": #만약에 하얀칸이 있는 자리에 말이있으면
        cnt += 1 #체크해준다.
print(cnt)
