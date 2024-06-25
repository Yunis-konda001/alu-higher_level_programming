#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = {key: val for key, val in a_dictionary.items() if val != value}
    print_sorted_dictionary(new_dict)
    print("--")
    return new_dict
