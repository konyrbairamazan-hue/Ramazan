import re  # Import the Regular Expression module

txt = "Hello, Abbracham" # The target string to search in

# re.findall: Finds all matches and returns them as a list
# r"ab*": The pattern. Matches 'a' followed by zero or more 'b's
# flags = re.IGNORECASE: Makes the search case-insensitive (A/a and B/b)
x = re.findall(r"ab*", txt, flags = re.IGNORECASE)

print(x) # Output: ['Abb', 'a', 'a']