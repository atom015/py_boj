a = set()
for i in range(int(input())):
    n,chk = input().split()
    if chk == "enter":a.add(n)
    else:a.remove(n)
for i in sorted(a)[::-1]:
    print(i)
#이문제 첫 실패이유 : 문제에서 동명이인이 없다는 부분에서 list가아니라
#set을 썻었어야 되는데 그러지 못했다.
#이문제 두번째 실패이유:remove할때 리스트에 인덱스가 아니라 그냥 n
#을 가져왔어야했는데 그러지 못했다.
#그리고 시간을 줄이기위해 del말고 remove를 썻어야했다