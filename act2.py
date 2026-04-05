def longest_consecutive_ones(n):
    count = 0
    max_count = 0
    
    while n > 0:
        if n & 1:  # check last bit
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
        n >>= 1  # right shift
    
    return max_count

# Example
num = int(input("Enter a number: "))
print("Longest consecutive 1s:", longest_consecutive_ones(num))