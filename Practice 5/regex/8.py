import re

txt = "HelloBro"

# (?=[A-Z]) -> This is a "Positive Lookahead".
# It looks for a position that is followed by a Capital Letter (A-Z),
# but it doesn't "consume" or delete that letter.
x = re.split("(?=[A-Z])", txt)

print(x) # Output: ['', 'Hello', 'Bro']