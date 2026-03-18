# A list of names to iterate through
names = ["Roma", "Maira", "Aibar"]
# enumerate() tracks both the index (i) and the value (name) at the same time
for i, name in enumerate(names):
    # i = the current position (starts at 0), name = the string from the list
    print(i, name)



a = [1, 2, 3]
b = [4, 5, 6]
# zip() pairs elements from both lists into tuples (1,4), (2,5), (3,6)
for x, y in zip(a, b):
    # x takes values from list 'a', y takes values from list 'b'
    print(x, y)