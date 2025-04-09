# asks the user for the fullname
# it counts characters in the name ignoring spaces
# salamus the user and inform them of the length of their name

# fullname = input ("Enter full name: ")
# letters = len(fullname.replace(" ", ""))
# print(f"Good morning {fullname}, your name has {letters} characters")



def salamu(*args):
    return args[0]

g = salamu("Mambo")
print(g)

def salamu(**kwargs):
    return kwargs['var']

g = salamu(var = "Hello")
print(g)

def salamu(*args, **kwargs):
    return args[0] + " " + kwargs['var']

g = salamu("Sema", var = "Hello")
print(g)














# def num_of_chrs_in_name(*args, **kwargs):
#     fname = len(kwargs['fname'])
#     lname = len(kwargs['lname'])
    
#     fullname = kwargs['fname'] + " " + kwargs['lname']
#     letters = fname + lname
    
#     print(f"Good morning {fullname},please {args[0]} {args[1]} {args[2]} you are {kwargs['age']} years old, your names have {letters} characters, phone number is {kwargs['phone']}")
    




# The data analyst in your company calculated the sales figures from last quater:
# increase_sales_percent = 12.9356
# increase_growth_percent = 18.564768
 
# using the above variables create a function that prints "Sales in our company went up by 12.94%, and our revenue has grown by 18.56 %"
















# h = 2.97683
# j = "john"
# print(f"h is {h:.2f}, and j is {j}")
# print("h is {:.2f}, and j is {}".format(h, j))
















# print("{:.3f}".format(h))

# print("h is {:.2f}".format(h))

# print("h is {:.2f}".format(h))







# Our company wants to block all emails not having the domain '@company.com'
# Create a function that asks the user for an email and decides whether it should be blocked or not



