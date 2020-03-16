Aat,Avi = map(int,input().split())
Bat,Bvi = map(int,input().split())
while Bvi > 0 and Avi > 0:
    Bvi -= Aat
    Avi -= Bat
print("PLAYER B" if Avi <= 0 < Bvi else ("PLAYER A" if Bvi <= 0 < Avi else "DRAW"))
