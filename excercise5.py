employee_data = [
    {"name": "Alice", "age": 30, "department": "HR", "salary": 50000},
    {"name": "Bob", "age": 45, "department": "IT", "salary": 70000},
    {"name": "Charlie", "age": 25, "department": "Finance", "salary": 60000},
    {"name": "Diana", "age": 35, "department": "IT", "salary": 75000},
    {"name": "Eve", "age": 40, "department": "HR", "salary": 52000},
]

def display_all_records(employee_data):
    print("\nAll Employee Records:")
    for emp in employee_data:
        print(f"Name: {emp['name']}, Age: {emp['age']}, Department: {emp['department']}, Salary: ${emp['salary']:.2f}")

def average_salary(employee_data):
    if not employee_data:
        print("No employee data available.")
        return 0
    total_salary = sum(emp['salary'] for emp in employee_data)
    avg_salary = total_salary / len(employee_data)
    print(f"\nAverage salary of all employees: ${avg_salary:.2f}")
    return avg_salary

def employees_in_age_range(employee_data, min_age, max_age):
    print(f"\nEmployees between ages {min_age} and {max_age}:")
    filtered = [emp for emp in employee_data if min_age <= emp['age'] <= max_age]
    if not filtered:
        print("No employees found in this age range.")
    for emp in filtered:
        print(f"Name: {emp['name']}, Age: {emp['age']}, Department: {emp['department']}, Salary: ${emp['salary']:.2f}")
    return filtered

def employees_in_department(employee_data, department):
    print(f"\nEmployees in department: {department}")
    filtered = [emp for emp in employee_data if emp['department'].lower() == department.lower()]
    if not filtered:
        print("No employees found in this department.")
    for emp in filtered:
        print(f"Name: {emp['name']}, Age: {emp['age']}, Salary: ${emp['salary']:.2f}")
    return filtered

def main():
    while True:
        print("\nEmployee Information System")
        print("1. Display all employee records")
        print("2. Display average salary")
        print("3. Display employees within an age range")
        print("4. Display employees within a department")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            display_all_records(employee_data)
        elif choice == '2':
            average_salary(employee_data)
        elif choice == '3':
            try:
                min_age = int(input("Enter minimum age: "))
                max_age = int(input("Enter maximum age: "))
                employees_in_age_range(employee_data, min_age, max_age)
            except ValueError:
                print("Invalid input! Please enter valid integers for age.")
        elif choice == '4':
            dept = input("Enter department name: ").strip()
            employees_in_department(employee_data, dept)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
