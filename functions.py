# def greet():
#     print('Hello World!')


# call the function
# greet()

# print('Outside function')

# Python Function Arguments
# def greet(name):
#     print("Hello", name)

# # pass argument
# greet("Mike")


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



# The dafault parameter value
# def my_cities(city = "Nairobi"):
#   print("I am from " + city)

# my_cities("kasarani")
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


def greet(fname, lname):
  print (f"Hello {fname} {lname}")
  
greet( "Otieno", lname = "Cliff")