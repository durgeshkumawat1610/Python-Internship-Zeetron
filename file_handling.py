
# File Handling Example
filename = "demo.txt"
with open(filename, 'w') as file:
    file.write("This is a file write example.")

with open(filename, 'r') as file:
    content = file.read()
    print("File Content:", content)
