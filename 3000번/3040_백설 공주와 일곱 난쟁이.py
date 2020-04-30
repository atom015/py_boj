def main(li,ms):
    for i in range(9):
        for j in range(9):
            if i != j:
                if 100 == ms-(li[i]+li[j]):
                    for k in li:
                        if k != li[i] and k != li[j]:
                            print(k)
                    return
num_li = []
for i in range(9):
    num_li.append(int(input()))
main(num_li,sum(num_li))
#이코드는 들어오는 숫자중 2개를 골라 들어오는 모든숫자에 합이랑 빼서 100이면 출력하게하는 코드이다.
