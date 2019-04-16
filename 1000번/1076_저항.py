color = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
value = [0,1,2,3,4,5,6,7,8,9]
mul = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000
]
input_color = []
Po = []
for i in range(3):
    input_color.append(input())
for i in range(3):
    if i == 2:
        Po.append(mul[color.index(input_color[i])])
    else:
        Po.append(value[color.index(input_color[i])])
result = int(str(Po[0])+str(Po[1]))*Po[2]
print(result)