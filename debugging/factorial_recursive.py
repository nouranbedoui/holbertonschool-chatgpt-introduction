#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function to calculate the factorial of a number recursively.

    Parameters:
    n (int): The number for which we need to calculate the factorial.

    Returns:
    int: The factorial of the number `n`. If n == 0, returns 1 as factorial of 0 is defined as 1.
    """
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n-1)  # Recursive case: n * factorial of n-1

# Read the input from the command line argument
f = factorial(int(sys.argv[1]))

# Print the computed factorial
print(f)
