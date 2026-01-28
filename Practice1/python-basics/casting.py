x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

a = bytes(5)                # b'\x00\x00\x00\x00\x00'
b = bytes("hello", "utf-8") # b'hello'

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

a = list((1, 2, 3))
b = list("hello")   # ['h', 'e', 'l', 'l', 'o']

a = set([1, 2, 2, 3])   # {1, 2, 3}
b = set("hello")       # {'h', 'e', 'l', 'o'}