# In programmin, polymorphism means the tendancy of an object to take many forms
# in greeK:
            # Poly means many
            # Morph means forms
class A:
    def show(self):
        print("from A")
class B(A): 
    def show(self):
        print("from B")
class C(A):
    def show(self):
        print("from C")
class D:
    def show(self):
        print("from D")
    ...
class E(B):
    ...
    
# obj1 = A()
obj1 = E()
# obj1.show()
# print(B.mro())
# print(E.mro())







# Example
# Without polimorphism
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def start(self):
        print("Car starting...")
        
    def stop(self):
        print("Car stoping...")
        
class Lorry:
    def __init__(self, brand, model, num_of_doors):
        self.brand = brand
        self.model = model
        self.doors = num_of_doors
        
    def start(self):
        print("Lorry starting...")
        
    def stop(self):
        print("Lorry stoping...")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     
# With polimorphism
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def start(self):
        print("Vehicle starting...")
        
    def stop(self):
        print("Vehicle stoping...")

        
class Car(Vehicle):
    def __init__(self, brand, model, num_of_doors):
        super().__init__(brand, model)
        self.num_of_doors = num_of_doors
        
    def start(self):
        print("Car starting...")
        
    def stop(self):
        print("Car stoping...")
        
class Lorry(Vehicle):
    def __init__(self, brand, model, num_of_doors):
        super().__init__(brand, model)
        self.doors = num_of_doors
        
    def start(self):
        print("Lorry starting...")
        
    def stop(self):
        print("Lorry stoping...")
       
car = Car("Corolla", "Toyota", 4)
lorry = Lorry("Fao", "Tata", 2)

# vehicles: [car, lorry]
vehicles: list[Vehicle] = [car, lorry]

for vehicle in vehicles:
    if isinstance(vehicle, Vehicle):
        print({type (vehicle).__name__})
        print(vehicle.brand)
        print(vehicle.model)
        # vehicle.stop()
        