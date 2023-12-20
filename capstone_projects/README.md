# Expense Management System

## Project Description

The Expense Management System is a python project that demonstrates object-oriented programming (OOP) concepts. It includes two classes, `Expense` and `ExpenseDB`, designed to model and manage financial expenses.

### Expense Class

Represents an individual financial expense.

#### Attributes:

1. `id`: A unique identifier generated as a UUID string.
2. `title`: A string representing the title of the expense.
3. `amount`: A float representing the amount of the expense.
4. `created_at`: A timestamp indicating when the expense was created (UTC).
5. `updated_at`: A timestamp indicating the last time the expense was updated (UTC).

#### Methods:

1. `__init__`: Initializes the attributes.
2. `update`: Allows updating the title and/or amount, updating the `updated_at` timestamp.
3. `to_dict`: Returns a dictionary representation of the expense.

### Expense Database Class

Manages a collection of `Expense` objects.

#### Attributes:

1. `expenses`: A list storing `Expense` instances.

#### Methods:

1. `__init__`: Initializes the list.
2. `add_expense`: Adds an expense.
3. `remove_expense`: Removes an expense.
4. `get_expense_by_id`: Retrieves an expense by ID.
5. `get_expense_by_title`: Retrieves expenses by title.
6. `to_dict`: Returns a list of dictionaries representing expenses.


## How to Clone the Project

To clone this project, run the following command in your terminal:

```bash
git clone https://github.com/your-username/expense-management-system.git


## Dummy Data Example Script

The `dummy_data_example.py` script demonstrates the usage of the Expense Management System classes with a predefined set of dummy data.

### Running the Script

To execute the script, run the following command in your terminal:

```bash
cd capstone_projects
python dummy_data_example.py


### Expected Outputs:
1. Printing All Expenses
The script will print details of all expenses stored in the ExpenseDB. For example;


2. Printing an Expense by ID (User Input Required)
The script will prompt the user to enter the ID of the expense they want to retrieve. If a valid ID is entered, it will print the details of the specific expense. For example;




3. Printing Expenses by Title
The script will print details of expenses with a specific title (in this case, "Utilities"):

### Handling Incorrect ID
If an incorrect or non-existent ID is entered, the script will notify the user that the expense was not found;




