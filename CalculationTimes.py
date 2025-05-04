# List of calculation times in milliseconds
calculation_times = [120, 50, 300, 200, 90, 10]

# Empty list to store sorted times
sorted_times = []

# Repeat until the original list is empty
while len(calculation_times) > 0:
    # Assume the first time is the smallest
    smallest = calculation_times[0]
    # Find the smallest time in the list
    for time in calculation_times:
        if time < smallest:
            smallest = time
    # Add the smallest time to the sorted list
    sorted_times.append(smallest)
    # Remove the smallest time from the original list
    calculation_times.remove(smallest)

# Print the sorted list
print("Calculation times sorted from fastest to slowest:")
print(sorted_times)
