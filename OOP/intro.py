class Human:
    identity = "Man"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
        
    def __str__(self):
        return f"{self.name} is a {self.age} years old {self.identity}"
        
human1 = Human("Ojwang", 56)
human2 = Human("Kwelld", 36)
print(human1)
print(human2)
