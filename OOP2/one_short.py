# object => A 'bundle' of related attributes(variables) and methods(function)
#            You need a keyword 'class' to create many objects
# A class is like a blueprint used to design the structure and layout of an object

class Car:
    num_of_wheels = 4 # class variable
    def __init__(self, model, year, color, for_sale): #constructor
        # Initialize attributes
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    # method
    def drive(self):
        print("Can drive now")
    
car_1 = Car("Mustang", 2014, "red", False) #instance of car class(object 1)
print(car_1.model)
print(Car.num_of_wheels)
car_1.num_of_wheels = 2
print(car_1.num_of_wheels)
car_1.drive()