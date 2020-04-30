def main(li,s):
    for i in range(9):
        for j in range(9):
            if i != j:
                if 100 == s-(li[i]+li[j]):
                    for k in sorted(li):
                        if k != li[i] and k != li[j]:
                            print(k)
                    return
num_li = []
for i in range(9):
    num_li.append(int(input()))
main(num_li,sum(num_li))
#이문제는 백설공주와 일곱난쟁이랑 비슷한 브루트 포스문제이다.
