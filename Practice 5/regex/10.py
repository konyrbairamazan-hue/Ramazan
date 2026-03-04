import re

txt = "CamelToSnake"

# r"([A-Z])" -> Finds every Capital letter and puts it in "Group 1" using ().
# r"_\1"     -> Replaces that letter with an underscore (_) followed by 
#               the same letter found in Group 1 (\1).
# .lower()   -> Converts the entire resulting string to lowercase.

x = re.sub(r"([A-Z])", r"_\1", txt).lower()

print(x) # Output: _camel_to_snake