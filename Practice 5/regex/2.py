import re

txt = "abbb abb ab"

# re.findall: Finds all occurrences that match the pattern
# r"ab{2,3}": The pattern. Matches 'a' followed by 'b' exactly 2 to 3 times
x = re.findall(r"ab{2,3}", txt)

print(x) # Output: ['abbb', 'abb']