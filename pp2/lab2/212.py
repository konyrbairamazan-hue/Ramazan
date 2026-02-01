n=int(input())
arr=list(map(int, input().split()))
for i in range(n):
    print(pow(arr[i], 2), end=" ")
