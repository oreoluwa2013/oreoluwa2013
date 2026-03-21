# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Find the maximum
max_num = max(num1, num2)

# Loop until LCM is found
while True:
    if max_num % num1 == 0 and max_num % num2 == 0:
        print("LCM:", max_num)
        break
    max_num += 1