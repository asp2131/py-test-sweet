# Python Unit Testing Practice

### A Beginner's Guide to Python's unittest Framework

**Table of Contents**

- [Before You Start](#before-you-start)
  - [Objective](#objective)
  - [Requirements and Grading](#requirements-and-grading)
  - [unittest: A Brief Overview](#unittest-a-brief-overview)
- [Lesson Steps](#lesson-steps)
  - [TODO 1: Create Your First Test Case](#todo-1-create-your-first-test-case)
  - [TODO 2: Test Numeric Functions](#todo-2-test-numeric-functions)
  - [TODO 3: Test String Functions](#todo-3-test-string-functions)
  - [TODO 4: Run Tests with Command Line](#todo-4-run-tests-with-command-line)
  - [CHALLENGE: Create a Test Suite](#challenge-create-a-test-suite)

<br><br>

# Before You Start

## **Objective**

In this project, you'll learn how to write and run unit tests using Python's built-in `unittest` framework. You'll create test cases for different types of functions, learn to handle exceptions in tests, and understand the core concepts of test-driven development.

You'll be learning to:

- **Write basic test cases** that validate functions work as expected
- **Implement different assertion methods** to check various conditions
- **Run tests** from the command line with various options

By the end, you'll have a solid foundation in writing unit tests with Python's unittest framework, a skill essential for creating reliable software. Let's get started! 🐍

<br><br>

## **Requirements and Grading**

This project includes specific requirements that focus on both understanding and implementing unit tests with Python's unittest framework.

---

## **Requirements and Grading**

| Requirement                                | Description                                                                                                      | Points |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- | ------ |
| **TODO 1: Create Your First Test Case**    | Create a basic test class and write your first test method for a simple function.                                | 25%    |
| **TODO 2: Test Numeric Functions**         | Implement tests for functions that perform mathematical operations, using appropriate numeric assertions.        | 25%    |
| **TODO 3: Test String Functions**          | Write tests for string manipulation functions using string-appropriate assertion methods.                        | 25%    |
| **TODO 4: Run Tests with Command Line**    | Learn to execute tests using command-line options and interpret test results effectively.                        | 25%    |

<br><br>

## **unittest: A Brief Overview**

Python's `unittest` framework is inspired by JUnit and provides tools for creating and running tests. It offers a rich set of assertion methods to check for and report failures. The framework is built into the Python standard library, so there's no need to install additional packages.

Key components of `unittest` include:

- **TestCase Class**: The basic building block for test cases.
- **Assertion Methods**: Methods like `assertEqual()`, `assertTrue()`, and others that test specific conditions.

- **Test Runner**: A component that orchestrates the execution of tests and provides the outcome to the user.

---

### Key Terms

<div style="width: 80%; margin: auto;">

| Term                | Definition                                                                                                      |
| ------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Unit Testing**    | Testing individual components or functions of software in isolation.                                            |
| **Test Case**       | A class containing test methods that validate specific parts of the code.                                       |
| **Assertion**       | A statement that a condition must be true; if false, the test fails.                                            |
| **Test Suite**      | A collection of test cases that work together.                                                                  |
| **Test Runner**     | The program that runs the tests and reports results.                                                            |

</div>

---

### Example

Here's a simple example of a unittest test case. This code tests a basic function that adds two numbers:

```python
import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
        
    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)
        
if __name__ == '__main__':
    unittest.main()
```

In this example:

- We define a simple `add` function that adds two numbers.
- We create a test class `TestAddFunction` that inherits from `unittest.TestCase`.
- Inside the test class, we define three test methods that test different scenarios.
- Each test uses the `assertEqual` method to check if the `add` function returns the expected result.
- Finally, we run the tests with `unittest.main()`.

# Lesson Steps

For this project, you'll learn how to create and run unit tests using Python's unittest framework. You'll start with simple test cases and progressively work with more advanced features like setup/teardown methods and testing for exceptions.

<br><br>

### Step-by-Step Work Flow

1. 📂 **Clone this repository** to begin working with the test files.

2. **Follow each TODO carefully** as you implement tests:
   - For each TODO, read the instructions carefully before writing code.
   - Only write code within the designated sections.

3. 🖥️ **Run your tests frequently** to check that they behave as expected.

---

<table style="width: 80%; margin-left: auto; margin-right: auto; border-collapse: collapse; margin-top: 15px; background-color: #2c2c2c; border: 1px solid #444; border-radius: 8px; overflow: hidden;">
  <tr>
    <th style="text-align: left; padding: 10px; background-color: #444; color: #e2e2e2; border-bottom: 1px solid #666;">
      💡 Key Reminders
    </th>
  </tr>
  <tr>
    <td style="padding: 10px; color: #e2e2e2;">
      - 📖 Read each TODO carefully to understand what you need to test.<br>
      - 🖥️ Run your tests after completing each TODO to ensure they pass.<br>
      - 📚 Use the unittest documentation if you get stuck. It's a great resource!
    </td>
  </tr>
</table>

---

<br>

### ✅ **Check Your Work!**

- **After each TODO**, run your tests to make sure they pass.
- If a test fails, review your code and fix any issues before moving on.

<!-- 4 line breaks between TODOs -->

<br><br><br><br>

## **TODO 1: Create Your First Test Case**

🎯 **Goal:** Create a basic test class and write your first test method for a simple function.

---

### Step-by-Step Instructions

1. **Open the `test_basics.py` file**

   - In this file, you'll find the `is_even()` function that checks if a number is even.
   - Your task is to create a test class to test this function.

2. **Create a Test Class**

   - Define a class called `TestBasics` that inherits from `unittest.TestCase`.
   - This class will contain all your test methods for the basic functions.

3. **Write Your First Test Method**

   - Create a method called `test_is_even`.
   - Inside this method, use the `assertTrue()` assertion to test that `is_even(2)` returns `True`.
   - Also, use the `assertFalse()` assertion to test that `is_even(3)` returns `False`.

4. **Add a Main Block**
   - At the end of the file, add the standard code block to make the file executable:
   ```python
   if __name__ == '__main__':
       unittest.main()
   ```

---

### ✅ **Check Your Work!**

Run your test file with:
```bash
python test_basics.py
```

You should see output indicating that your test passed!

<br><br><br><br>

## **TODO 2: Test Numeric Functions**

🎯 **Goal:** Write tests for functions that perform mathematical operations.

---

### Step-by-Step Instructions

1. **Open the `test_numeric.py` file**

   - In this file, you'll find two functions: `add()` that adds two numbers, and `multiply()` that multiplies two numbers.
   - Your task is to create tests for these functions.

2. **Create a Test Class**

   - Define a class called `TestNumeric` that inherits from `unittest.TestCase`.

3. **Test the Add Function**

   - Create a method called `test_add`.
   - Use the `assertEqual()` assertion to test the following cases:
     - `add(2, 3)` should return `5`
     - `add(-1, 1)` should return `0`
     - `add(-1, -1)` should return `-2`

4. **Test the Multiply Function**
   - Create a method called `test_multiply`.
   - Use the `assertEqual()` assertion to test the following cases:
     - `multiply(2, 3)` should return `6`
     - `multiply(-1, 1)` should return `-1`
     - `multiply(-1, -1)` should return `1`

---

### ✅ **Check Your Work!**

Run your test file with:
```bash
python test_numeric.py
```

Your tests should pass if the functions work correctly.

<br><br><br><br>

## **TODO 3: Test String Functions**

🎯 **Goal:** Write tests for string manipulation functions.

---

### Step-by-Step Instructions

1. **Open the `test_strings.py` file**

   - In this file, you'll find two functions: `concatenate()` that joins two strings, and `reverse()` that reverses a string.
   - Your task is to create tests for these functions.

2. **Create a Test Class**

   - Define a class called `TestStrings` that inherits from `unittest.TestCase`.

3. **Test the Concatenate Function**

   - Create a method called `test_concatenate`.
   - Use the `assertEqual()` assertion to test the following cases:
     - `concatenate("Hello, ", "World!")` should return `"Hello, World!"`
     - `concatenate("", "Python")` should return `"Python"`
     - `concatenate("Test", "")` should return `"Test"`

4. **Test the Reverse Function**
   - Create a method called `test_reverse`.
   - Use the `assertEqual()` assertion to test the following cases:
     - `reverse("hello")` should return `"olleh"`
     - `reverse("Python")` should return `"nohtyP"`
     - `reverse("")` should return `""`

---

### ✅ **Check Your Work!**

Run your test file with:
```bash
python test_strings.py
```

Your tests should pass if the functions work correctly.

<br><br><br><br>

## **TODO 4: Run Tests with Command Line**

**Goal:** Learn to run tests using command-line options and interpret test results.

---

### Step-by-Step Instructions

1. **Open the `run_tests.py` file**

   - This file will demonstrate how to discover and run tests using Python's unittest framework.

2. **Run All Tests**

   - Use the following command to run all tests in the directory:
   ```bash
   python -m unittest discover
   ```

3. **Run Tests with Verbose Output**

   - Use the `-v` flag to get more detailed output:
   ```bash
   python -m unittest discover -v
   ```

4. **Run a Specific Test Module**

   - Run only the tests in a specific file:
   ```bash
   python -m unittest test_basics
   ```

5. **Run a Specific Test Case**
   - Run only a specific test case:
   ```bash
   python -m unittest test_basics.TestBasics
   ```

6. **Run a Specific Test Method**
   - Run only a specific test method:
   ```bash
   python -m unittest test_basics.TestBasics.test_is_even
   ```

---

### ✅ **Check Your Work!**

Try each of the command-line options and observe the differences in the output. This will help you understand how to run tests efficiently in different scenarios.

<br><br><br><br>

## **CHALLENGE: Create a Test Suite**

🎯 **Goal:** Combine multiple test cases into a test suite.

---

### Step-by-Step Instructions

1. **Open the `test_suite.py` file**

   - In this file, you'll create a test suite that includes tests from multiple test classes.

2. **Import Test Classes**

   - Import the test classes from the previous TODO tasks.

3. **Create a Test Suite**

   - Use `unittest.TestSuite()` to create a new test suite.
   - Add test cases to the suite using `addTest()`.

4. **Run the Test Suite**
   - Use `unittest.TextTestRunner().run(suite)` to run the test suite.

---

### ✅ **Check Your Work!**

Run your test suite with:
```bash
python test_suite.py
```

You should see output indicating which tests were run as part of the suite.



### Push Reminder

That's it! You've completed a comprehensive introduction to Python's unittest framework. 🎉 Don't forget to push your changes to your repository!