n=int(input())
arr=list(map(int, input().split()))
mx=arr[0]
mn=arr[0]
for i in range(n):
    if arr[i] > mx:
        mx = arr[i]
    if arr[i] < mn:
        mn = arr[i]
for i in range(n):
    if arr[i] == mx:
        arr[i] = mn
print(*arr)