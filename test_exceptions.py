def divide(a, b):
    """
    Divide two numbers.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        The result of a / b
        
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Your task is to create a test class that tests the divide function, including exception handling
# Don't forget to import unittest at the top!

import unittest

# TODO: Create a TestExceptions class that inherits from unittest.TestCase

# TODO: Write a test_normal_division method that tests normal division

# TODO: Write a test_division_by_zero method that tests division by zero

# TODO: Add code to run the tests if this file is executed directly