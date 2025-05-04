def calculate_file_info(file_sizes):
    number_of_files = len(file_sizes)
    
    total_memory = 0
    for size in file_sizes:
        total_memory += size 
    
    if number_of_files == 0:
        average_size = 0
    else:
        average_size = total_memory / number_of_files
    
    return number_of_files, total_memory, average_size

files = [150, 80, 220, 95, 300]
count, total, average = calculate_file_info(files)

print("file Count:",count)
print("total Memory Used:", total,"MB")
print("average File Size:", round(average, 2),"MB")