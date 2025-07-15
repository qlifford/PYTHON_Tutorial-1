# def greet():
#     print('Hello World!')


# # call the function
# greet()
# del greet
# greet()

# print('Outside function')

# Python Function Arguments
# def salam(**kwrgs):
#     print(f"{kwrgs['fname']} {kwrgs['mname']} {kwrgs['lname']}")

# # pass argument
# salam(fname="Wamboi", mname="kamau", lname= "joy")






# # # function with two arguments
# # def add_numbers(num1, num2):
# #     sum = num1 + num2
# #     print("Sum: ", sum)

# # # function call with two values
# # add_numbers(5, 4)


# # function with two arguments
# def add_numbers(num1, num2):
#     sum = num1 + num2
#     print("Sum: ", sum)

# # Function call with two values
# # Function to Add Two Numbers
# def add_numbers(num1, num2):
#     result = num1 + num2
#     print("Sum: ", result)

# add_numbers(2, 5)

# The return Statement
# We return a value from the function using the return statement.

# # function definition
# def find_square(num):
#     result = num * num
#     return result

# # function call
# square = find_square(3)

# print('Square:', square)

# The pass Statement
# The pass statement serves as a placeholder for future code, preventing errors from empty code blocks.
# It's typically used where code is planned but has yet to be written.

# def future_function():
#     pass

# # this will execute without any action or error
# future_function()  

# def is_prime(n):
#     if n % 2 == 0:
#         print(f"{n} is a prime number")
#     else:
#         print(f"{n} is NOT a prime number")        

# b = int(input("Enter a number: "))
# is_prime(b)



# # The dafault parameter value
# def my_cities(city = "Nairobi", **kwargs):
#   print(f"I am from {city} {kwargs['state']}\nI speak {kwargs['lang']}" )

# my_cities(city="Kakamega", state = "kenya", lang = "kiswahili")
# my_cities("karen")
# my_cities()
# my_cities("umoja")

# # Arguments(args(tuple)) 
# def my_function(*args):
#   print("The first child is " + kids[0])

# my_function("John", "Emil", "Tobias", "Linus")

# Keyword arguments(kwargs(dictionary))
# def my_function(**kwargs):
#   print("Last name is " + kwargs["lname"])
#   print("Age is " + str(kwargs["age"]))

# my_function(fname = "Cliff", lname = "Omollo", age = 40)

# def addresses(**kwargs):
#   # for value in kwargs.values():
#   # for key in kwargs.keys():
#   # for item in kwargs.items():
#   for key, value in kwargs.items():
#     print (f"{key}: {value}")
#     # print (item)
#   # print(type(kwargs))
  
# addresses(city='nairobi', location='town', phone='1234')


# def greet(fname, lname):
#   print (f"Hello {fname} {lname}")
  
# greet( "Otieno", lname = "Cliff")


# # Scope of variables
# # Variable with global scope
# name = "Python"
# def func():
#     print("Inside the function, the value of name is:", name)
# print("Outside the function, the value of name is:", name)

# func()

# # Variable with local scope








# var = 20 #global variable
# def func(): 
#     global v   
#     v = 20 #local variable
#     print(f"{v} inside")

# func()

# print(f'{v} outside')




# # print("Outside the function, the value of var is:", var)


# num = 10 # lifeline is global
# def func():
#     num = 5 # lifeline ends in here
#     print("Inside the function, the value of num is:", num)
# print("Before executing the function")
# print("num=", num)

# func()

# print("After executing the function")
# print("num=", num)



# A lambda is one line function
# print(lambda a, b:a + b)







# def my_func(x, y):
#     result = x * y
#     return result  


# print(my_func(5, 5)) 

 
# mlt = lambda x, y, z: x * y + z
# print(mlt(5, 5, 4))











# nums = [1, 15, 3, 6, 22, 10]
# max = nums[0]
# def largest_num(num, max ):
#     for num in nums:
#         if num > max:
#             max = num
#     print(max)


# largest_num()









# max = nums[0]
# for num in nums:
#     if num > max:
#         max = num
# print(max)       
















# Nested functions
# def outer_function():
#     print("Outer function")
    
#     def inner_function():
#         print("Inner function")
#     inner_function()
    
# outer_function()

def f1(name):
    salam = "hi, {}".format(name).capitalize()
    def f2():
        print (salam)
    f2()
    

        

        
