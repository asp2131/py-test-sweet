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

# Your task is to create a test class that tests the ShoppingCart class using setUp and tearDown
# Don't forget to import unittest at the top!

import unittest

# TODO: Create a TestShoppingCart class that inherits from unittest.TestCase

# TODO: Implement setUp method to create a new cart before each test

# TODO: Implement tearDown method to clean up after each test

# TODO: Write a test_add_item method that tests adding items to the cart

# TODO: Write a test_calculate_total method that tests the calculate_total method

# TODO: Add code to run the tests if this file is executed directly