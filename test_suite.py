import unittest

# CHALLENGE: Import test classes from your previous test files

# TODO: Import test classes from previous files
# from test_basics import TestBasics
# from test_numeric import TestNumeric
# from test_strings import TestStrings

def create_test_suite():
    """
    Create a test suite containing all test cases.
    
    Returns:
        A test suite with all test cases
    """
    # TODO: Create a test suite
    
    
    # TODO: Add test cases to the suite
    # suite.addTest(unittest.makeSuite(TestBasics))
    # suite.addTest(unittest.makeSuite(TestNumeric))
    # etc...
    
    return suite

if __name__ == '__main__':
    # TODO: Run the test suite
    suite = create_test_suite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)