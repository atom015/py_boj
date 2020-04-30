for i in range(int(input())):
    h,m,a,d,ch,cm,ca,cd = map(int,input().split())
    hp = h+ch
    mp = m+cm
    attack = a+ca
    defence = d+cd
    if hp < 1:
        hp = 1
    if mp < 1:
        mp = 1
    if attack < 0:
        attack = 0
    print(1*hp+5*mp+2*attack+2*defence)
