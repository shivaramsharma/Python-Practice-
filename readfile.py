#Write a program to read a file and print the longest line

try:
    with open('interviews.txt', 'r') as file:
        lines = file.readlines()
    if not lines:
        print("file is empty")
    else:
        longest_line = ""
        max_length = 0
        for line in lines:
            if len(line) > max_length:
                max_length = len(line)
                longest_line = line
    print(f"The longest line (length {max_length}) is:\n---")
    print(longest_line.strip())
    print("---")

except FileNotFoundError:
     print("Error: The file 'your_file.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
