class Em ployee():

    def _init_(self, first_name, middle_name, last_name, salary):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.salary = salary


employee_1 = Employee("Alex", None,"Smith", 82000)
employee_2 = Employee("Brad", None, "Smill", 82000)
employee_3 = Employee("Chad", None, "Will", 82000)
employee_3 = Employee("Chad", None, "allison", "Will", 82000)

employees = [employee_1, employee_2, employee_3]

for employee in employees:
    print(f"first name: {employee.first_name}, last name: {employee.last_name}, salary: {employee.salary}")