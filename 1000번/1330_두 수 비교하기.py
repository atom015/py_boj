a,b = map(int,input().split())
def compare(a,b):
    if a < b: #b가 a보다 크면
        return '<' #"<"출력
    elif a > b: #a가 b보다 크면
        return ">" #">"출력
    return "==" #같으면 "==출력"
print(compare(a,b))
