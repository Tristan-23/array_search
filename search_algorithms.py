import time
import random

# Linear Search Function
def linear_search(array, target):
    for element in array:
        if element == target:
            return True
    return False

# Binary Search Function
def binary_search(array, target, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, low, mid - 1)
    else:
        return binary_search(array, target, mid + 1, high)

# Generate a larger sorted array of 100,000 random numbers
array_size = 100000
random_array = sorted(random.sample(range(1, 200000), array_size))  # Ensuring sorted random numbers
target = random.choice(random_array)  # Choosing a random target from the array

# Number of iterations to improve timing accuracy
iterations = 1000

# Timing Linear Search over multiple iterations
linear_search_time_total = 0
for _ in range(iterations):
    start_time = time.time()
    linear_search(random_array, target)
    linear_search_time_total += time.time() - start_time
linear_search_time_avg = linear_search_time_total / iterations

# Timing Binary Search over multiple iterations
binary_search_time_total = 0
for _ in range(iterations):
    start_time = time.time()
    binary_search(random_array, target, 0, len(random_array) - 1)
    binary_search_time_total += time.time() - start_time
binary_search_time_avg = binary_search_time_total / iterations

# Output average results with 6 decimal places
print(f"Average Linear Search Time: {linear_search_time_avg:.6f} seconds")
print(f"Average Binary Search Time: {binary_search_time_avg:.6f} seconds")
print(f"Target number: {target}")
