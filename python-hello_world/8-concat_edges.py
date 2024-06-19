#!/usr/bin/env python3

# Define the required string
original_string = "object-oriented programming with Python"

# Slice the string to split it into components
part1 = original_string[:18]  # "object-oriented "
part2 = original_string[18:31]  # "programming "
part3 = original_string[31:]  # "with Python"

# Concatenate the parts with new words to form a new sentence
new_sentence = part1 + part2 + part3 + "\n"

# Print the new sentence
print(new_sentence)
