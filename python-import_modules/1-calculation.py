#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

def main():
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    # Perform the calculations and store the results
    addition_result = add(a, b)
    subtraction_result = sub(a, b)
    multiplication_result = mul(a, b)
    division_result = div(a, b)

    # Print the results
    print(f"{a} + {b} = {addition_result}")
    print(f"{a} - {b} = {subtraction_result}")
    print(f"{a} * {b} = {multiplication_result}")
    print(f"{a} / {b} = {division_result}")

if __name__ == "__main__":
    main()
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
