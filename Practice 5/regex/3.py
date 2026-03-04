import re

txt = "aa_b ddd_aa eeeff"

# re.findall: Finds all occurrences that match the pattern
# r"[a-z]+_[a-z]+": The pattern. 
#   [a-z]+ : One or more lowercase letters
#   _      : Followed by an underscore
#   [a-z]+ : Followed by one or more lowercase letters
x = re.findall(r"[a-z]+_[a-z]+", txt)

print(x) # Output: ['aa_b', 'ddd_aa']