import csv 

class EmployeeManager:

    def __init__ (self):
        self.employees={}
        self.csv_to_read()

    def add_employee(self):
        try:
           employee_id =int(input("Enter your ID : "))
        except ValueError:
            print("only numeric values , please")
            return

        name =input ("Enter your name :")
        position =input ("Enter your Position :")
        try:
            salary = float(input ("Enter your Salary :"))
        except ValueError:
            print("only numeric values , please")
            return
        if salary <0:
            print("Salary cannot be negative")
            return
        email = input("Enter your Email :")

        if employee_id in self.employees:
           print("This employee  already exists")
           return
        
        self.employees[employee_id]={"name":name ,"position":position ,"salary":salary ,"email":email}
        self.save_to_csv()
        print("Employee added successfully")
  

    def save_to_csv(self):
        with open("employees.csv","w",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID","name","position","salary","email"])
            for employee_id,employee in self.employees.items():
                writer.writerow([
                    employee_id,
                    employee["name"],
                    employee["position"],
                    employee["salary"],
                    employee["email"]
                ])
    def view_employees(self):
        for employee_id , employee in self.employees.items():
            print(f"ID:{employee_id} ,name :{employee['name']},position :{employee['position']} , salary:{employee['salary']} , email :{employee['email']}")

    def search_employee(self):
        try:
           employee_id = int(input ("ID :"))
        except ValueError:
            print("only numeric values , please")
            return
        if employee_id in self.employees:
            employee = self.employees[employee_id]
            print(f"ID:{employee_id} ,name :{employee['name']},position :{employee['position']} , salary:{employee['salary']} , email :{employee['email']}")
        else:
            print("employee isn't exist")
        
    def update_employee(self):
        try:
           employee_id = int(input ("ID :"))
        except ValueError:
            print("only numeric values , please")
            return
        if employee_id in self.employees:
            employee = self.employees[employee_id]
            name =input ("Enter your name :")
            if name =="":
                name = employee["name"]

            position =input ("Enter your Position :")
            if position =="":
                position = employee["position"]

            salary = input ("Enter your Salary :")
            if salary == "":
                salary = employee["salary"]
            else:
                try:
                   salary = float(salary)
                   if salary <0:
                       print("only positive salary")
                       return
                except ValueError:
                    print("only numeric values , please")
                    return

            email = input("Enter your Email :")
            if email =="":
                email = employee["email"]

            employee["name"] = name
            employee["position"] = position
            employee["salary"] = salary
            employee["email"] = email
            self.save_to_csv()
            print("Employee updated successfully")
        else:
            print("employee isn't exist")

    def delete_employee(self):
        try:
           employee_id = int(input ("ID :"))
        except ValueError:
            print("only numeric values , please")
            return
        if employee_id in self.employees:
            del self.employees[employee_id]
            self.save_to_csv()
            print("Employee deleted successfully")

        else:
            print("employee isn't exist")

    def csv_to_read(self):
        try:
            with open ("employees.csv","r")as file:
                reader= csv.reader(file)
                next(reader)
                for row in reader :
                    employee_id, name, position, salary, email = row
                    employee_id=int(employee_id)
                    salary=float(salary)
                    self.employees[employee_id] ={"name":name ,"position":position ,"salary":salary ,"email":email}
        except FileNotFoundError:
            print("the file not found")

    def employee_menu(self):
        while True:
            print("1. Add Employee")
            print("2. View All Employees")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Search Employee")
            print("6. Exit")
            choice = input("choose :")
            if choice =="1":
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
                print("Thank you for using program ")
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.employee_menu()