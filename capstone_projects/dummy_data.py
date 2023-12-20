from expense import Expense, ExpenseDB

# Using a dummy data to demonstrate how these classes can be used
expenses_data = [
    {"title": "Groceries", "amount": 200000},
    {"title": "Utilities", "amount": 100000},
    {"title": "Wife", "amount": 2000000}
]

# Creating an ExpenseDB instance and populating it with dummy data
expense_db = ExpenseDB()
for expense_info in expenses_data:
    new_expense = Expense(title=expense_info["title"], amount=expense_info["amount"])
    expense_db.add_expense(new_expense)

# Print all expenses
print("\nPrinting all expenses:")
for expense in expense_db.expenses:
    print(expense.to_dict())

try:
    # User input for expense by ID (Since for every run of the expense script, a new uuid is generated, pasting newly generated ID is a good option)
    user_input_id = input("\nEnter the ID of the expense you want to retrieve (paste the ID here): ")
    found_expense = expense_db.get_expense_by_id(user_input_id)

    # Print an expense by ID
    print("\nPrinting expense by ID:")
    if found_expense:
        print(found_expense.to_dict())
    else:
        print("Expense not found. Make sure it's a valid ID")
except Exception as e:
    print(f"An error occurred: {e}")

# Print expenses by title
print("\nPrinting expenses by title:")
expenses_by_title = expense_db.get_expenses_by_title("Utilities")
for expense in expenses_by_title:
    print(expense.to_dict())