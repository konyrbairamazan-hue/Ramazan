n=int(input())
arr=list(map(int, input().split()))
s=set()

for i in arr:
    if i not in s:
        print("YES")
        s.add(i)
    else:
        print("NO")