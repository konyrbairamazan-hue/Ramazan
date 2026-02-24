#1
import math

degree = int(input("Input degree: "))
radian = degree * (math.pi / 180)
print("Output radian: "f"{radian:.6}")

#2
import math

height = int(input("Height: "))
first = int(input("Base, first value: "))
second = int(input("Base, second value: "))
area = (first + second) * height / 2
print("Expected Output: " f"{area}")

#3 
import math

sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))

area = (sides * length ** 2) / (4 * math.tan(math.pi / sides))

print("The are of the polygon is: "f"{area:.0f}")

#4 
import math

base = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))
area = base * height
print("Expected Output: "f"{area:.1f}")