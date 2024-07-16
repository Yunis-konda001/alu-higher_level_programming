#!/usr/bin/python3
"""append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after each line containing search_string in the file."""
    
    with open(filename, "r", encoding="utf-8") as readFile:
        lines = readFile.readlines()

    with open(filename, "w", encoding="utf-8") as writeFile:
        for line in lines:
            writeFile.write(line)
            if search_string in line:
                writeFile.write(new_string)

# Test case:
# Let's create a temporary file for testing

filename = "test_file.txt"
search_string = "c"
new_string = "Python is cool!\n"

# Write initial content to the file
with open(filename, "w", encoding="utf-8") as file:
    file.write("c is fun!")

# Apply the function
append_after(filename, search_string, new_string)

# Read and print the result to verify the output
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()

print(content)

