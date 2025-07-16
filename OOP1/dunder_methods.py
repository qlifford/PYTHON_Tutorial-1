# Dunder methods also called special methods are found within a classe, they start with two underscores and end with two underscores e.g __str__, __init__. 
# They are automatically called by many of python's built-in operations and allow developers define or customize the behavior of objects

class Student:
    def __init__(self, name, gpa):
        self.n = name
        self.gpa = gpa        
        
    def __str__(self):
        return f'\nName: {self.n}\nGpa: {self.gpa}\n'
    
    def __eq__(self, other):
        return self.n == other.n and self.gpa == other.gpa
    
    def __add__(self, other):
        return self.gpa + other.gpa
    
    def __contains__(self, keyword):
        return keyword in self.n
    
    def __getitem__(self, key):
        if key == 'name':
            return self.n
        elif key == 'gpa':
            return self.gpa
        else:
            return f"'{key}' was not found!"
    
std1 = Student("Coffee", 8.5)
std2 = Student("Coffee", 8.5)
std3 = Student("Davie", 7.5)
# print(std1 == std3)
print(std1 + std3)
# print(std1)
# print(std2)
# print('C' in std1)
# print('C' in std3)
print(std3['name'])
print(std3['gpa'])
print(std3['xy'])