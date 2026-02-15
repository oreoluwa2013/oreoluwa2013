# File operations example in Python

file_name = "example.txt"

# 1. Write to a file (creates file if it doesn't exist)
with open(file_name, "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    file.write("Python file handling example.\n")

print("File written successfully.\n")

# 2. Read the entire file
with open(file_name, "r") as file:
    content = file.read()
    print("Full File Content:")
    print(content)

# 3. Read file line by line
with open(file_name, "r") as file:
    print("Reading line by line:")
    for line in file:
        print(line.strip())

# 4. Append to the file
with open(file_name, "a") as file:
    file.write("This line was appended.\n")

print("\nContent after appending:")

with open(file_name, "r") as file:
    print(file.read())

# 5. Count number of lines
with open(file_name, "r") as file:
    lines = file.readlines()
    print(f"Number of lines: {len(lines)}")

# 6. Search for a word
search_word = "Python"
with open(file_name, "r") as file:
    found = any(search_word in line for line in file)

if found:
    print(f"'{search_word}' found in file.")
else:
    print(f"'{search_word}' not found in file.")
