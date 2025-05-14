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

# CHALLENGE: Create a test class for BankAccount
# Don't forget to import unittest at the top!

import unittest

# TODO: Create a TestBankAccount class that inherits from unittest.TestCase

# TODO: Implement setUp method to create a new account before each test

# TODO: Write test methods for:
#  - test_initialization: Test the initial balance is set correctly
#  - test_deposit: Test depositing money works correctly
#  - test_withdraw: Test withdrawing money works correctly
#  - test_insufficient_funds: Test that withdrawing too much raises an error

# TODO: Add code to run the tests if this file is executed directly