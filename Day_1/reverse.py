def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap elements at the left and right positions
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# Example usage:
my_array = [1, 2, 3, 4, 5]
reverse_array(my_array)
print(my_array)  # Output: [5, 4, 3, 2, 1]
