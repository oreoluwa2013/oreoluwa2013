# File name
file_name = "example.txt"

# 1. Read mode ("r") - Opens file for reading (file must exist)
try:
    with open(file_name, "r") as file:
        content = file.read()
        print("Read Mode Content:")
        print(content)
except FileNotFoundError:
    print("File not found for read mode.")

# 2. Write mode ("w") - Creates new file or overwrites existing file
with open(file_name, "w") as file:
    file.write("This is written using write mode.\n")
    print("\nFile written in write mode.")

# 3. Append mode ("a") - Adds content to the end of the file
with open(file_name, "a") as file:
    file.write("This line is appended.\n")
    print("File updated in append mode.")

# 4. Read and Write mode ("r+") - Opens for reading and writing (file must exist)
try:
    with open(file_name, "r+") as file:
        print("\nRead+Write Mode Content Before Writing:")
        print(file.read())
        file.write("Adding text using r+ mode.\n")
except FileNotFoundError:
    print("File not found for r+ mode.")

# 5. Write and Read mode ("w+") - Overwrites file and allows reading
with open(file_name, "w+") as file:
    file.write("This file is opened in w+ mode.\n")
    file.seek(0)  # Move pointer to beginning for reading
    print("\nWrite+Read Mode Content:")
    print(file.read())

# 6. Append and Read mode ("a+") - Appends and allows reading
with open(file_name, "a+") as file:
    file.write("Appending with a+ mode.\n")
    file.seek(0)
    print("\nAppend+Read Mode Content:")
    print(file.read())

