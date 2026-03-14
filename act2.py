def myfunction(n):

    # First Loop → O(n)
    for i in range(0, n+1):
        print("First Loop")

    # Second Loop → O(log n)
    j = 1
    while (j <= n+1):
        print("Second Loop", j)
        j = j * 2

    # Third Loop → O(1)
    for i in range(0, 100):
        print("Third Loop")


# call the function
myfunction(10)

# Time Complexity:
# O(n) + O(log n) + O(1) = O(n)