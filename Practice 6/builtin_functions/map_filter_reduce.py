numbers = [1, 2, 3, 4]
# map() applies the lambda function (x*2) to every item in the 'numbers' list
result = list(map(lambda x: x * 2, numbers))
# lambda x: x*2 is an anonymous function that takes 'x' and returns 'x multiplied by 2'
print(result)


numbers = [1, 2, 3, 4, 5]
# filter() keeps only the elements where the lambda condition is True
result = list(filter(lambda x: x % 2 == 0, numbers))
# x % 2 == 0 checks if a number is even (remainder is zero when divided by 2)
print(result)