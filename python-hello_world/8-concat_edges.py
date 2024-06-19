#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"

# Extract the required parts
part1 = str[39:57]  # "object-oriented"
part2 = str[58:69]  # "programming"
part3 = str[0:6] + str[114] + str[81:86]  # " with Python"

# Concatenate and print the result
print(part1 + " " + part2 + part3)
