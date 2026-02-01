n = int(input())
arr = [input().strip() for _ in range(n)]

first_occurrence = {}


for i, word in enumerate(arr):
    if word not in first_occurrence:
        first_occurrence[word] = i + 1 

for word in sorted(first_occurrence):
    print(word, first_occurrence[word])
