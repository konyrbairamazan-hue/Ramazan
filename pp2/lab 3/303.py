s = input().strip()

to_digit = {
    "ZER":"0", "ONE":"1", "TWO":"2", "THR":"3",
    "FOU":"4", "FIV":"5", "SIX":"6", "SEV":"7",
    "EIG":"8", "NIN":"9"
}

to_word = {
    "0":"ZER", "1":"ONE", "2":"TWO", "3":"THR",
    "4":"FOU", "5":"FIV", "6":"SIX", "7":"SEV",
    "8":"EIG", "9":"NIN"
}

for i, c in enumerate(s):
    if c in "+-*":
        pos = i
        op = c
        break

A = s[:pos]
B = s[pos+1:]

n1 = ""
for i in range(0, len(A), 3):
    n1 += to_digit[A[i:i+3]]

n2 = ""
for i in range(0, len(B), 3):
    n2 += to_digit[B[i:i+3]]

x = int(n1)
y = int(n2)

if op == "+":
    res = x + y
elif op == "-":
    res = x - y
else:
    res = x * y

ans = ""
for c in str(res):
    ans += to_word[c]

print(ans)