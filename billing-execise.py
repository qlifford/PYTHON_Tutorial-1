# You have been asked to create a program that will automatically calculate the bill for a pizza sale service.
# pizza sizes are small, medium and large
# small pizza is $35, medium pizza is $40 and large pizza is $45
# peperoni for small pizza is $2, for medium pizza is $2 and for large pizza is $3
# extra cheese is $1


size = input("Enter the size of pizza s/m/l: ")
pepperoni = input("Add pepperoni y/n: ")
extra_cheese = input("Add extra cheese y/n: ")


bill = 0
if size == "s":
    bill += 35
elif size == "m":
    bill += 40
else:
    bill += 45

if pepperoni == "y":
    if size == "s" or size == "m":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is Ksh {bill} only")