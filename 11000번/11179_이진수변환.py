n = int(input())
ch = format(n,'b')[::-1]
print(int(ch,2))
#format(n,'b') == 십진수 이진수변환
#int(ch,2) == 이진수 십진수변환,ch = 이진수,2 = 이진수로 바꾼다는뜻
