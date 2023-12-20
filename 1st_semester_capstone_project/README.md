# My Expense Management System

## Project Description

My Expense Management System is a python project that demonstrates object-oriented programming (OOP) concepts. It includes two classes, `Expense` and `ExpenseDB`, designed to model and manage financial expenses.

### Expense Class

Represents my financial expenses.

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

Manages a collection of my `Expense` objects.

#### Attributes:

1. `expenses`: A list storing my `Expense` instances.

#### Methods:

1. `__init__`: Initializes the list.
2. `add_expense`: Adds an expense.
3. `remove_expense`: Removes an expense.
4. `get_expense_by_id`: Retrieves an expense by ID.
5. `get_expense_by_title`: Retrieves expenses by title.
6. `to_dict`: Returns a list of dictionaries representing expenses.


## How to Clone the Project

If you would love to clone my systen or this project for keeping track of your expenses, you should run the following command on your terminal:

```bash
git clone https://github.com/Tsegalion/ALT_SCHOOL.git
```

### Running the Script
The `expense.py` script creates the Expense and ExpenceDB classes. To execute the script, you should run the following command in your terminal:

```bash
cd 1st_semester_capstone_project # to navigate to the project directory:
python expense.py # to run the expense script
```

### Expected Outputs:
After running the code, you can expect the following functionality:

`Expense Class`:

An Expense object is created with a unique identifier `id`, `title`, `amount`, and timestamps for creation `created_at` and last update `updated_at`.
The `update method` allows you to modify the `title` and/or `amount` of the expense, updating the `updated_at` timestamp to the current time.
The `to_dict` method converts an Expense object into a dictionary.

`ExpenseDB`: An ExpenseDB object is created to serve as a container for managing expenses.

`Adding a New Expense`:
The `add_expense` method is used to add a new expense to the database. For instance, a grocery expense with a `title` of "Groceries" and an `amount` of $50.00 or expense titled "Wife" with an amount of $1000.00 is added.

`Removing an Expense by ID`:
The `remove_expense` method allows the removal of a specific expense based on its unique identifier (ID). For example, the expense with ID "8e444faa-b4a9-4a68-a089-d7fe552475ff" is removed from the database.

`Retrieving an Expense by ID`:
The `get_expense_by_id` method retrieves an expense from the database based on its unique identifier (ID). For instance, the expense with ID "1c981f83-8990-43d3-8090-ab8e5e2e3d98" is retrieved.

`Retrieving Expenses by Title`:
The `get_expenses_by_title` method retrieves a list of expenses with a specific title. For example, all expenses with the `title` "Wife" are retrieved.

`Converting to Dictionary`:
The `to_dict` method is used to convert the entire ExpenseDB object, including all stored expenses, into a list of dictionaries.

The above actions collectively demonstrate the basic functionality of `my expense management system`, allowing you to `add`, `remove`, and `retrieve` expenses based on different criteria.