import re

txt = "Hello, beko"

# [A-Z]  -> Matches exactly one Uppercase letter (A-Z)
# [a-z]+ -> Matches one or more lowercase letters (a-z)
x = re.findall("[A-Z][a-z]+", txt)

print(x) # Output: ['Hello']