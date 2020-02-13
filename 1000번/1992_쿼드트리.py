n = int(input())
arr = [list(map(int,input())) for i in range(n)]
def checking(size,x,y):
	for i in range(x,x+size):
		for j in range(y,y+size):
			if arr[i][j] != arr[x][y]:
				return False
	return True
def divison(x,y,size):
	if checking(size,x,y):
		print(arr[x][y],end="")
	else:
		print("(",end="")
		new = size//2
		divison(x,y,new)
		divison(x,y+new,new)
		divison(x+new,y,new)
		divison(x+new,y+new,new)
		print(")",end="")


divison(0,0,n)
