def find_largest_file(file_sizes):
    if not file_sizes:
        return "no files receieved"
    
    biggest = file_sizes[0]
    for current_size in file_sizes:
        if current_size > biggest:
            biggest = current_size
            
    return biggest

files = [150, 80, 220, 95, 300]
result = find_largest_file(files)
print(f"the largest file is{result}")
