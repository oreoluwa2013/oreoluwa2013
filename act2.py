def get_substrings(s):
    substrings = []
    n = len(s)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])
    
    return substrings

# Example
string = input("Enter a string: ")
result = get_substrings(string)

print("All substrings:")
for sub in result:
    print(sub)