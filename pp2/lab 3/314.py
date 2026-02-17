n = int(input())
arr = list(map(int, input().split()))
q = int(input())

funcs = []

for _ in range(q):
    op = input().split()

    if op[0] == "add":
        x = int(op[1])
        funcs.append(lambda a, x=x: a + x)

    elif op[0] == "multiply":
        x = int(op[1])
        funcs.append(lambda a, x=x: a * x)

    elif op[0] == "power":
        x = int(op[1])
        funcs.append(lambda a, x=x: a ** x)

    else:
        funcs.append(lambda a: abs(a))


for f in funcs:
    arr = list(map(f, arr))

print(*arr)