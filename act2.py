def reverse_bits(n, bit_size=32):
    reversed_num = 0
    
    for i in range(bit_size):
        # Shift reversed_num left
        reversed_num <<= 1
        
        # Add the last bit of n
        reversed_num |= (n & 1)
        
        # Shift n right
        n >>= 1
    
    return reversed_num

# Example usage
num = int(input("Enter a number: "))
result = reverse_bits(num)

print("Reversed bits number:", result)