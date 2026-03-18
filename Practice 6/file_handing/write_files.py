# A list of strings, each ending with \n (newline) to start a new line
lines = ["First line\n", "Second line\n"]

# Open 'output.txt' in 'w' (write) mode. This overwrites existing content!
with open('output.txt', 'w', encoding='utf-8') as f:
    # f.writelines() takes a list and writes all its items to the file
    f.writelines(lines)
    
    # f.write() adds a single string to the end of the current position
    f.write("Additional text")