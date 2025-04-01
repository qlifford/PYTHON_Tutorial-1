size = input("Enter pizza size?S or M or L: ").lower()
pepperoni = input("Add pepperoni?N or Y: ").lower()
extra_cheese = input("Add extra cheese?N or Y: ").lower()
# bill = 0
if size == "s":
    bill = 15
elif size == "m":
    bill = 20
else:
    bill = 25

if pepperoni == "y":
    if size == "s" or size == "m":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    if size == "m" or size == "l":
        bill += 5
    else:
        bill += 1


print(f"Your total bill is Kshs {bill}")

