# The 'with' statement is the safest way to open files — it auto-closes them
with open('example.txt', 'r', encoding='utf-8') as f:
    # f.read() loads the entire file content into the 'content' variable
    content = f.read()
    print(content)