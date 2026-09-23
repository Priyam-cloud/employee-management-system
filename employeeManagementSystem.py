"""
Employee Management System (EMS)

A simple console-based employee management system
built using Python dictionaries, functions, loops,
conditional statements, and input validation.

Features:
1. Add Employee
2. View All Employees
3. Search for Employee
4. Exit
"""


# Step 1 - Data Storage

employees = {
    101: {
        "name": "Satya",
        "age": 27,
        "department": "HR",
        "salary": 50000
    },
    102: {
        "name": "Rahul",
        "age": 30,
        "department": "IT",
        "salary": 60000
    }
}


# Step 3 - Add Employee

def add_employee():

    print("\n===== Add Employee =====")

    emp_id = int(input("Enter Employee ID: "))

    while emp_id in employees:
        print("Employee ID already exists.")
        emp_id = int(
            input("Please enter a different Employee ID: ")
        )

    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = float(input("Enter Employee Salary: "))

    employees[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }

    print("Employee added successfully!")


# Step 4 - View All Employees

def view_employees():

    print("\n===== All Employees =====")

    if not employees:
        print("No employees available.")
        return

    print("-" * 75)

    print(
        f"{'ID':<10}"
        f"{'Name':<20}"
        f"{'Age':<10}"
        f"{'Department':<20}"
        f"{'Salary':<15}"
    )

    print("-" * 75)

    for emp_id, employee in employees.items():

        print(
            f"{emp_id:<10}"
            f"{employee['name']:<20}"
            f"{employee['age']:<10}"
            f"{employee['department']:<20}"
            f"{employee['salary']:<15}"
        )

    print("-" * 75)


# Step 5 - Search Employee

def search_employee():

    print("\n===== Search Employee =====")

    emp_id = int(input("Enter Employee ID: "))

    if emp_id in employees:

        employee = employees[emp_id]

        print("\nEmployee Found!")
        print("Employee ID :", emp_id)
        print("Name        :", employee["name"])
        print("Age         :", employee["age"])
        print("Department  :", employee["department"])
        print("Salary      :", employee["salary"])

    else:
        print("Employee not found.")


# Step 2 & Step 6 - Main Menu

def main_menu():

    while True:

        print("\n========================================")
        print("     Employee Management System")
        print("========================================")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            print(
                "\nThank you for using Employee Management System!"
            )
            break

        else:
            print("\nInvalid choice. Please try again.")


# Start the program

if __name__ == "__main__":
    main_menu()