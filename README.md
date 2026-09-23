# Employee Management System (EMS)

A simple **console-based Employee Management System** built with Python.

This project was created as a Python learning project to practice **dictionaries, functions, loops, conditional statements, input handling, and basic program structure**.

## 📌 Project Objective

The objective of this project is to create a simplified Employee Management System that allows users to:

1. Add an employee
2. View all employees
3. Search for an employee by ID
4. Exit the application

Employee data is stored using a Python dictionary, where the **Employee ID** is used as the key and the employee's details are stored in a nested dictionary.

## ✨ Features

### 1. Add Employee

Users can enter:

* Employee ID
* Employee Name
* Employee Age
* Employee Department
* Employee Salary

The program checks whether the Employee ID already exists before adding the employee.

### 2. View All Employees

Displays all employees in a table-like format containing:

* Employee ID
* Name
* Age
* Department
* Salary

If there are no employees, the program displays:

```text
No employees available.
```

### 3. Search Employee

Users can search for an employee using their Employee ID.

If the employee exists, the program displays their details.

If the employee does not exist:

```text
Employee not found.
```

### 4. Exit

The program displays a thank-you message and exits when the user selects the Exit option.

## 🛠️ Technologies Used

* Python 3
* Python Dictionaries
* Functions
* `if/elif/else`
* `while` loop
* `for` loop
* User Input
* Basic Input Validation

## 📂 Project Structure

```text
employee-management-system/
│
├── employeeManagementSystem.py
├── README.md
├── .gitignore
└── screenshots/
    ├── menu.png
    ├── add_employee.png
    ├── view_employees.png
    └── search_employee.png
```

## ▶️ How to Run

### Prerequisites

Install **Python 3** on your computer.

Check your Python installation:

```bash
python --version
```

or:

```bash
python3 --version
```

### Run the Application

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Move into the project directory:

```bash
cd employee-management-system
```

Run the program:

```bash
python employee_management_system.py
```

## 💻 Example

```text
========================================
     Employee Management System
========================================
1. Add Employee
2. View All Employees
3. Search for Employee
4. Exit
========================================
Enter your choice:
```

### Example — View Employees

```text
===== All Employees =====
---------------------------------------------------------------------------
ID        Name                Age       Department          Salary
---------------------------------------------------------------------------
101       Satya               27        HR                  50000
102       Rahul               30        IT                  60000
---------------------------------------------------------------------------
```

## 📚 Concepts Practiced

This project helped me practice:

* Variables
* Dictionaries
* Nested dictionaries
* Functions
* Function calls
* `if`, `elif`, and `else`
* `while` loops
* `for` loops
* `.items()`
* `input()`
* Type conversion using `int()` and `float()`
* String formatting
* Basic input validation
* Program organization

## 🎯 Learning Outcome

Through this project, I learned how to build a small command-line application using Python and how different Python concepts work together in a complete program.

## 🚀 Future Improvements

Possible future improvements include:

* Update employee details
* Delete an employee
* Save employee data to a file
* Use JSON or SQLite for persistent storage
* Add stronger input validation
* Create a graphical user interface
* Add object-oriented design using classes

## 👤 Author

**Priyam Kumari**

This project is part of my Python learning and project development journey.
