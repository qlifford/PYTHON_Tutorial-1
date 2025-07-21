class Employee:
    raise_amount = 300
    num_employees = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        Employee.num_employees += 1
        # self.num_employees += 1
        # self.__class__.num_employees += 1

    def __str__(self):
        return f"Name: {self.name},\nSalary: {self.salary}\n"
      
    def apply_raise(self):
      self.salary += self.raise_amount
      # self.salary += Employee.raise_amount
      
      
employee_1 = Employee("John", 50000)
employee_2 = Employee("Cliff", 20000)

# print(Employee.name)

print(employee_1)
print(employee_2)

employee_1.raise_amount = 500
employee_1.apply_raise()

print(Employee.raise_amount)
print(employee_1.raise_amount)

print(Employee.num_employees)
# print(employee_1.num_employees)
