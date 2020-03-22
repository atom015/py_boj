arr1 = [int(input()) for i in range(3)]
arr2 = [int(input()) for i in range(3)]
p1 = arr1[0]*3+arr1[1]*2+arr1[2]
p2 = arr2[0]*3+arr2[1]*2+arr2[2]
print("B" if p1 < p2 else ("A" if p1 > p2 else "T"))
