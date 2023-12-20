import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self, title, amount):
        # Initialize attributes for Expense class
        self.id = str(uuid.uuid4()) # Generate a unique identifier using UUID
        self.title = title  # Title of the expense
        self.amount = amount  # Amount of the expense
        self.created_at = datetime.utcnow() # Current timestamp when the expense is created
        self.updated_at = self.created_at # Initialize updated_at with created_at for the first time

    def update(self, title=None, amount=None):
        # Method to update title and/or amount of the expense
        self.title = title if title is not None else self.title
        self.amount = amount if amount is not None else self.amount
        self.updated_at = datetime.utcnow() # Update the updated_at timestamp to the current time

    def to_dict(self):
        # Method to convert Expense object to a dictionary
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

class ExpenseDB:
    def __init__(self):
        # Initialize attributes for ExpenseDB class
        self.expenses = []

    def add_expense(self, expense):
        # Method to add an expense to the database
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        # Method to remove an expense from the database by ID
        self.expenses = [ex for ex in self.expenses if ex.id != expense_id]

    def get_expense_by_id(self, expense_id):
        # Method to retrieve an expense from the database by ID
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expenses_by_title(self, title):
        # Method to retrieve expenses from the database by title (returning a list)
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self):
        # Method to convert ExpenseDB object to a list of dictionaries
        return [expense.to_dict() for expense in self.expenses]