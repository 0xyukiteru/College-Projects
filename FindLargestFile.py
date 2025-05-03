def find_largest_file(file_sizes):
    if not file_sizes:
        return None  # Return None if list is empty
    largest = file_sizes[0]
    for size in file_sizes:
        if size > largest:
            largest = size
    return largest

# Example usage
example_files = [120, 450, 300, 700, 250]
largest_file = find_largest_file(example_files)
print("Largest file size:", largest_file)

