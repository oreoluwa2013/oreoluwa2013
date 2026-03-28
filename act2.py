def rightmost_set_bit(n):
    if n == 0:
        return 0
    return n & -n

# Example usage
num = int(input("Enter a number: "))
result = rightmost_set_bit(num)

print("Rightmost set bit value:", result)