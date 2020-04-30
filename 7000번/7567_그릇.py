result = 10
input_str = list(input())
for i in range(1, len(input_str)):
    if input_str[i] == input_str[i-1]:
        result += 5
    else:
        result +=10
print(result)
