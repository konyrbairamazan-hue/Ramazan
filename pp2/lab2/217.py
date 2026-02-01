from collections import Counter

n = int(input())
numbers = [input().strip() for _ in range(n)]

count = Counter(numbers)


result = sum(1 for v in count.values() if v == 3)

print(result)
