import re

txt = "aaeeerrb aaaasudeei"

# a    -> Starts with 'a'
# .*?  -> Matches any character (.) zero or more times (*),
#         but as FEW as possible (?) (Lazy match)
# b    -> Ends with 'b'
x = re.findall("a.*?b", txt)

print(x) # Output: ['aaeeerrb']