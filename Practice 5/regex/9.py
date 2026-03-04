import re

txt = "HelloCapHowAreYou?"

# re.sub(pattern, replacement, string)
# (?=[A-Z]) -> This is a "Positive Lookahead".
# It matches a POSITION (a gap) that is followed by a capital letter (A-Z).
# It does NOT replace the letter; it just finds the spot before it.
x = re.sub("(?=[A-Z])", ' ', txt)

print(x) # Output: " Hello Cap How Are You?"