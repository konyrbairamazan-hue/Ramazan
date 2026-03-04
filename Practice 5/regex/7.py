import re

txt = "Snake_to_Camel"

# r"_([a-zA-Z])" -> Matches an underscore AND the letter after it.
# The parentheses () capture only the letter into "Group 1".

# lambda x: x.group(1).upper() -> Takes the captured letter, 
# converts it to uppercase, and removes the underscore.

x = re.sub(r"_([a-zA-Z])", lambda x: x.group(1).upper(), txt)

print(x) # Output: SnakeToCamel