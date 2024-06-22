#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

def main():
    a = 10
    b = 5

    # Perform the calculations
    addition_result = add(a, b)
    subtraction_result = sub(a, b)
    multiplication_result = mul(a, b)
    division_result = div(a, b)

    # Print the results using only 4 print statements
    print(f"{a} + {b} = {addition_result}")
    print(f"{a} - {b} = {subtraction_result}")
    print(f"{a} * {b} = {multiplication_result}")
    print(f"{a} / {b} = {division_result}")

if __name__ == "__main__":
    main()
