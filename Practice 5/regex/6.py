import re

txt = "Hello, Jon. How are you?"

# re.sub(pattern, replacement, string)
# [\s.,] -> A character class that matches:
#   \s  : Any whitespace (space)
#   .   : A literal dot
#   ,   : A literal comma
x = re.sub("[\s.,]", ":", txt)

print(x) # Output: Hello::Jon::How:are:you?