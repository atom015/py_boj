n = int(input())
nli = sorted(list(map(int,input().split()))) #리스트 정렬
m = int(input())
mli = list(map(int,input().split()))
def binary_search_recursion(target,low,high,data):
    if low > high: #만약에 시작지점이 끝지점보다 크면
        return 0 #None return
    mid = (low+high)//2
    if data[mid] == target:
        return 1
    elif data[mid] > target:
        high = mid - 1
    else:
        low = mid + 1
    return binary_search_recursion(target,low,high,data)
for i in mli:
    print(binary_search_recursion(i,0,n-1,nli))
"""
target : 찾고자 하는 값
data : 오름차순으로 정렬된 list
start : data 의 처음 값 인덱스
end : data 의 마지막 값 인덱스
mid : start, end 의 중간 인덱스
"""
