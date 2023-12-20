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
```

## Dummy Data Example Script

The `dummy_data_example.py` script demonstrates the usage of the Expense Management System classes with a predefined set of dummy data.

### Running the Script

To execute the script, run the following command in your terminal:

```bash
cd capstone_projects
python dummy_data_example.py
```

### Expected Outputs:
1. Printing All Expenses
The script will print details of all expenses stored in the ExpenseDB. For example;

```bash
{'id': '1c981f83-8990-43d3-8090-ab8e5e2e3d98', 'title': 'Groceries', 'amount': 200000, 'created_at': datetime.datetime(2023, 12, 20, 18, 6, 53, 845683), 'updated_at': datetime.datetime(2023, 12, 20, 18, 6, 53, 845683)}
{'id': '2e6e9ca9-5541-4231-ad31-e1db465f7d1c', 'title': 'Utilities', 'amount': 100000, 'created_at': datetime.datetime(2023, 12, 20, 18, 6, 53, 845683), 'updated_at': datetime.datetime(2023, 12, 20, 18, 6, 53, 845683)}
{'id': '8e444faa-b4a9-4a68-a089-d7fe552475ff', 'title': 'Wife', 'amount': 2000000, 'created_at': datetime.datetime(2023, 12, 20, 18, 6, 53, 845683), 'updated_at': datetime.datetime(2023, 12, 20, 18, 6, 53, 845683)}
```

2. Printing an Expense by ID (User Input Required)
The script will prompt the user to enter the ID of the expense they want to retrieve. If a valid ID is entered, it will print the details of the specific expense. For example;

```bash
Enter the ID of the expense you want to retrieve (paste the ID here): 8e444faa-b4a9-4a68-a089-d7fe552475ff

Printing expense by ID:
{'id': '8e444faa-b4a9-4a68-a089-d7fe552475ff', 'title': 'Wife', 'amount': 2000000, 'created_at': datetime.datetime(2023, 12, 20, 18, 16, 33, 577902), 'updated_at': datetime.datetime(2023, 12, 20, 18, 16, 33, 577902)}
```

3. Printing Expenses by Title
The script will print details of expenses with a specific title (in this case, "Utilities"):
```bash
Printing expenses by title:
{'id': '8c0cc2c3-3e8e-4ef7-8e6e-f4445bedba55', 'title': 'Utilities', 'amount': 100000, 'created_at': datetime.datetime(2023, 12, 20, 18, 16, 33, 577902), 'updated_at': datetime.datetime(2023, 12, 20, 18, 16, 33, 577902)}
```

### Handling Incorrect ID
If an incorrect or non-existent ID is entered, the script will notify the user that the expense was not found;

```bash
Printing all expenses:
{'id': '48889a06-17be-476c-a173-5494294c05f2', 'title': 'Groceries', 'amount': 200000, 'created_at': datetime.datetime(2023, 12, 20, 18, 18, 26, 693030), 'updated_at': datetime.datetime(2023, 12, 20, 18, 18, 26, 693030)}
{'id': 'd89b067e-9478-44e3-9d2e-996f67a04802', 'title': 'Utilities', 'amount': 100000, 'created_at': datetime.datetime(2023, 12, 20, 18, 18, 26, 693030), 'updated_at': datetime.datetime(2023, 12, 20, 18, 18, 26, 693030)}
{'id': 'ea96b6d0-d820-42be-8a3f-7f783caf3e81', 'title': 'Wife', 'amount': 2000000, 'created_at': datetime.datetime(2023, 12, 20, 18, 18, 26, 693030), 'updated_at': datetime.datetime(2023, 12, 20, 18, 18, 26, 693030)}

Enter the ID of the expense you want to retrieve (paste the ID here): 22828e8dcdfnfjfj99393

Printing expense by ID:
Expense not found. Make sure it's a valid ID

Printing expenses by title:
{'id': 'd89b067e-9478-44e3-9d2e-996f67a04802', 'title': 'Utilities', 'amount': 100000, 'created_at': datetime.datetime(2023, 12, 20, 18, 18, 26, 693030), 'updated_at': datetime.datetime(2023, 12, 20, 18, 18, 26, 693030)}
```