"""
This file demonstrates how to run tests with different command-line options.

Run all tests in the directory:
    python -m unittest discover

Run with verbose output:
    python -m unittest discover -v

Run a specific test module:
    python -m unittest test_basics

Run a specific test case:
    python -m unittest test_basics.TestBasics

Run a specific test method:
    python -m unittest test_basics.TestBasics.test_is_even
"""

import unittest

# The unittest module provides functions to discover and run tests
# You don't need to add code to this file - just use the commands shown above

# For example, uncomment the code below to run all tests in the directory
if __name__ == '__main__':
    unittest.main()