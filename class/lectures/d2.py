employees = []

employees.append({"first_name": "Alex", "last_name": "smith", "Salary": 87000})
employees.append({"first_name": "Brad", "last_name": "will", "Salary": 62})
employees.append({"first_name": "pablo", "last_name": "dayton", "Salary": 89000})

employees.append({"first_name": "bhaavia", "last_name": "sinha", "Salary": 73000})

employees.append({"first_name": "jones", "last_name": "anderson", "Salary": 98000})

employees.append({"first_name": "David", "last_name": "Jones", "Salary": 82000})


for employee in employees:
    print(f"First name: {employee['first_name']}, last name: {employee['last_name']}, salary: {employee['Salary']}")

print("Increasing salary...")
for employee in employees:
    employee["Salary"] = employee["Salary"] * 1.05

print("After increase")
for employee in employees:
    print(f"First name: {employee['first_name']}, last name: {employee['last_name']}, salary: {employee['Salary']}")