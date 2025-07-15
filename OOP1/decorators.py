# Decorator - Its a function that modifies the behavior of another function while not changing that functions functionality

def my_decorator(function):
    def wrapper():
        print("My decorator")
        function()
    return wrapper

@my_decorator
def my_function():
    print("My funcion")    
my_function()