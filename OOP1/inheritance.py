# Single inheritence
class Employee:
    def __init__(self, name):
        self.name = name
        
    def show(self):
        return "From single employee class"
        
class Teacher(Employee):
    ... 
        
teacher1 = Teacher("Jane")

print(teacher1.name)
print(teacher1.name)

# Multiple inheritence
class Employee:
    def __init__(self, name):
        self.name = name
        
    def show(self):
        return "From multiple employee class"
        
class Teacher:        
    def __init__(self, name):
        self.name = name
        
    def show(self):
        return "From teacher multiple class"
        
           
class Student(Employee, Teacher):
    ... 
        
student1 = Student("Jane")

print(student1.show())
print(Teacher.show(teacher1))


# Multilevel inheritence
class Employee:
    def __init__(self, name):
        self.name = name
        
    def show(self):
        return "From multilevel employee class"
        
class Teacher(Employee): 
    ...
           
class Student(Teacher):
    ... 
        
student1 = Student("Jane")

print(student1.name)
print(student1.show())
# print(Teacher.show(teacher1))

