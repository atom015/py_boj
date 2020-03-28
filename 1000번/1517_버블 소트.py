from sys import *
setrecursionlimit(10**9)
ip = stdin.readline
n = int(ip())
arr = list(map(int,ip().split()))
ret = 0
def merge(s,mid,e):
    global ret
    i,j,k = s,mid+1,s
    ans = []
    while i <= mid and j <= e:
        if arr[i] <= arr[j]:
            ans.append(arr[i])
            i += 1
        else:
            ans.append(arr[j])
            ret += (mid - i + 1) #(mid-i+1)은 왼쪽 배열에 있는 수만큼 바꾸기 때문이다.
            j += 1
    while j <= e:
        ans.append(arr[j])
        j += 1
    while i <= mid:
        ans.append(arr[i])
        i += 1
    arr[s:e+1] = ans
def mergeSort(s,e):
   if s < e:
        mid = (s+e)//2
        mergeSort(s,mid)
        mergeSort(mid+1,e)
        merge(s,mid,e)
mergeSort(0,n-1)
print(ret)
