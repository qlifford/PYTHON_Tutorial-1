# single inheritance
class Human:
    identity = "God's creation"  # Class attribute
    # Class attributes are shared by all instances of the class.
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
        
    def walk(self):
        print(f"{self.identity} can walk!")

    def speak(self):
        print( "I can speak!")
        
class Male(Human):
    def __init__(self, name, age, dance):
        super().__init__(name, age) 
        self.dance = dance
    def disp(self):
        print(f"{self.name} is a {self.age} years old {self.identity} and loves to dance to {self.dance} music.")
        # Inherits from Human
    def walk(self):
        super().walk()  # Call the parent class method
        # or you can override the method
        print("Male can walk!")

    # def speak(self):
    #     print( "Male can speak!")
        
m1 = Male("John Doe", 30, 'reggea')  
m1.walk()  # Output: I can walk!   
m1.disp()
# one parent
# multiple inheritance
# Multilevel inheritance
# Hyracheal inheritance