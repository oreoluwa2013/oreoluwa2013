def myfunction2(n):
    # Base case
    if (n <= 1):
        return
    
    # Constant operation
    print("Codingal")
    
    # Recursive call
    myfunction2(n-1)


# Example function call
myfunction2(5)

# Recurrence Relation:
# Each call performs O(1) work (print statement)
# and then calls the function with (n-1)

# T(n) = T(n-1) + O(1)

# Solving the recurrence:
# T(n) = O(n)