for i in range(int(input())):
    ox = list(input())
    cnt = [0 for i in range(len(ox))]
    for i in range(len(ox)):
        if ox[i] == "X":
            cnt[i] = 0
        elif ox[i] == "O":
            cnt[i] = cnt[i-1] + 1
    cnt = sum(cnt)
    print(cnt)
