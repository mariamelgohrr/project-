import csv
import os

class EmployeeManager:
    def __init__(self):
        self.employees = {}
        self.filename = "employees.csv"
        self.load_from_csv()

    def load_from_csv(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.employees[row["ID"]] = {
                        "Name": row["Name"],
                        "Position": row["Position"],
                        "Salary": row["Salary"],
                        "Email": row["Email"]
                    }

    def save_to_csv(self):
        with open(self.filename, "w", newline="") as file:
            fieldnames = ["ID", "Name", "Position", "Salary", "Email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for emp_id, data in self.employees.items():
                writer.writerow({
                    "ID": emp_id,
                    "Name": data["Name"],
                    "Position": data["Position"],
                    "Salary": data["Salary"],
                    "Email": data["Email"]
                })

    def add_employee(self):
        emp_id = input("Enter ID: ")
        if emp_id in self.employees:
            print("This ID already exists.")
            return

        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")

        if not salary.isdigit():
            print("Salary must be a number.")
            return

        email = input("Enter Email: ")

        self.employees[emp_id] = {
            "Name": name,
            "Position": position,
            "Salary": salary,
            "Email": email
        }
        self.save_to_csv()
        print("Employee added successfully.")

    def view_employees(self):
        if not self.employees:
            print("No employees found.")
            return

        for emp_id, data in self.employees.items():
            print("ID:", emp_id)
            print("Name:", data["Name"])
            print("Position:", data["Position"])
            print("Salary:", data["Salary"])
            print("Email:", data["Email"])
            print("------------------")

    def update_employee(self):
        emp_id = input("Enter the ID of the employee to update: ")
        if emp_id not in self.employees:
            print("Employee not found.")
            return

        print("Leave a field empty if you don't want to change it.")

        name = input("New Name: ")
        position = input("New Position: ")
        salary = input("New Salary: ")
        email = input("New Email: ")

        if name != "":
            self.employees[emp_id]["Name"] = name
        if position != "":
            self.employees[emp_id]["Position"] = position
        if salary != "":
            if salary.isdigit():
                self.employees[emp_id]["Salary"] = salary
            else:
                print("Salary must be a number, keeping old value.")
        if email != "":
            self.employees[emp_id]["Email"] = email

        self.save_to_csv()
        print("Employee updated successfully.")

    def delete_employee(self):
        emp_id = input("Enter the ID of the employee to delete: ")
        if emp_id not in self.employees:
            print("Employee not found.")
            return

        del self.employees[emp_id]
        self.save_to_csv()
        print("Employee deleted successfully.")

    def search_employee(self):
        emp_id = input("Enter the ID to search: ")
        if emp_id in self.employees:
            data = self.employees[emp_id]
            print("ID:", emp_id)
            print("Name:", data["Name"])
            print("Position:", data["Position"])
            print("Salary:", data["Salary"])
            print("Email:", data["Email"])
        else:
            print("Employee not found.")

    def run(self):
        while True:
            print("\n--- Employee Management System ---")
            print("1. Add Employee")
            print("2. View All Employees")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Search Employee")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.update_employee()
            elif choice == "4":
                self.delete_employee()
            elif choice == "5":
                self.search_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid option, try again.")


if __name__ == "__main__":
    manager = EmployeeManager()
    manager.run()