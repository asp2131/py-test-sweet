# Example Solutions

Here are example solutions for the unittest practice repository. Use these as a reference if you get stuck or want to compare your own solutions.

## test_basics.py Solution

```python
import unittest

def is_even(number):
    """
    Check if a number is even.
    
    Args:
        number: An integer to be checked
        
    Returns:
        bool: True if number is even, False otherwise
    """
    return number % 2 == 0

class TestBasics(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(-1))
        self.assertTrue(is_even(-2))

if __name__ == '__main__':
    unittest.main()
```

## test_numeric.py Solution

```python
import unittest

def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b

def multiply(a, b):
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The product of a and b
    """
    return a * b

class TestNumeric(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
```

## test_strings.py Solution

```python
import unittest

def concatenate(str1, str2):
    """
    Concatenate two strings.
    
    Args:
        str1: First string
        str2: Second string
        
    Returns:
        The concatenation of str1 and str2
    """
    return str1 + str2

def reverse(s):
    """
    Reverse a string.
    
    Args:
        s: String to reverse
        
    Returns:
        The reversed string
    """
    return s[::-1]

class TestStrings(unittest.TestCase):
    def test_concatenate(self):
        self.assertEqual(concatenate("Hello, ", "World!"), "Hello, World!")
        self.assertEqual(concatenate("", "Python"), "Python")
        self.assertEqual(concatenate("Test", ""), "Test")
        
    def test_reverse(self):
        self.assertEqual(reverse("hello"), "olleh")
        self.assertEqual(reverse("Python"), "nohtyP")
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse("a"), "a")

if __name__ == '__main__':
    unittest.main()
```

## test_fixtures.py Solution

```python
import unittest

class ShoppingCart:
    """
    A shopping cart that can store items and calculate the total cost.
    """
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []
    
    def add_item(self, name, price):
        """
        Add an item to the cart.
        
        Args:
            name: Name of the item
            price: Price of the item
        """
        self.items.append({"name": name, "price": price})
    
    def calculate_total(self):
        """
        Calculate the total price of all items in the cart.
        
        Returns:
            The total price
        """
        return sum(item["price"] for item in self.items)

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        """Create a new cart before each test."""
        self.cart = ShoppingCart()
        
    def tearDown(self):
        """Clean up after each test."""
        self.cart = None
        
    def test_add_item(self):
        self.cart.add_item("apple", 1.0)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["name"], "apple")
        self.assertEqual(self.cart.items[0]["price"], 1.0)
        
    def test_calculate_total(self):
        self.cart.add_item("apple", 1.0)
        self.cart.add_item("banana", 1.5)
        self.cart.add_item("orange", 2.0)
        self.assertEqual(self.cart.calculate_total(), 4.5)

if __name__ == '__main__':
    unittest.main()
```

## test_exceptions.py Solution

```python
import unittest

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

class TestExceptions(unittest.TestCase):
    def test_normal_division(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(10, -2), -5.0)
        
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

## test_suite.py Solution

```python
import unittest
from test_basics import TestBasics
from test_numeric import TestNumeric
from test_strings import TestStrings
from test_fixtures import TestShoppingCart
from test_exceptions import TestExceptions

def create_test_suite():
    """
    Create a test suite containing all test cases.
    
    Returns:
        A test suite with all test cases
    """
    suite = unittest.TestSuite()
    
    suite.addTest(unittest.makeSuite(TestBasics))
    suite.addTest(unittest.makeSuite(TestNumeric))
    suite.addTest(unittest.makeSuite(TestStrings))
    suite.addTest(unittest.makeSuite(TestShoppingCart))
    suite.addTest(unittest.makeSuite(TestExceptions))
    
    return suite

if __name__ == '__main__':
    suite = create_test_suite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
```

## test_custom_class.py Solution

```python
import unittest

class BankAccount:
    """
    A simple bank account class with deposit and withdrawal functionality.
    """
    
    def __init__(self, initial_balance=0):
        """
        Initialize a bank account with an initial balance.
        
        Args:
            initial_balance: Initial balance for the account (default 0)
        """
        self.balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount: Amount to deposit
            
        Returns:
            New balance
            
        Raises:
            ValueError: If amount is negative
        """
        if amount < 0:
            raise ValueError("Cannot deposit negative amount")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        """
        Withdraw money from the account.
        
        Args:
            amount: Amount to withdraw
            
        Returns:
            New balance
            
        Raises:
            ValueError: If amount is negative or greater than balance
        """
        if amount < 0:
            raise ValueError("Cannot withdraw negative amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)  # Start with $100
    
    def test_initialization(self):
        self.assertEqual(self.account.balance, 100)
        empty_account = BankAccount()
        self.assertEqual(empty_account.balance, 0)
    
    def test_deposit(self):
        new_balance = self.account.deposit(50)
        self.assertEqual(new_balance, 150)
        self.assertEqual(self.account.balance, 150)
        
        # Test depositing zero
        new_balance = self.account.deposit(0)
        self.assertEqual(new_balance, 150)
        
        # Test raising error for negative deposit
        with self.assertRaises(ValueError):
            self.account.deposit(-50)
    
    def test_withdraw(self):
        new_balance = self.account.withdraw(50)
        self.assertEqual(new_balance, 50)
        self.assertEqual(self.account.balance, 50)
        
        # Test withdrawing zero
        new_balance = self.account.withdraw(0)
        self.assertEqual(new_balance, 50)
        
        # Test raising error for negative withdrawal
        with self.assertRaises(ValueError):
            self.account.withdraw(-50)
    
    def test_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(150)  # More than we have

if __name__ == '__main__':
    unittest.main()
```