import random




user_choice = int(input("Enter your choice\n0 for Rock\n1 for Paper\n2 for Scissors:\n"))
comp_choice = random.randint(0, 2)
print("Computer choice: ", comp_choice)

if user_choice == comp_choice:
    print("It's a tie!")
elif comp_choice == 0 and user_choice == 2:
    print("You win!")
elif comp_choice == 2 and user_choice == 0:
    print("You lose!")
elif comp_choice > user_choice:
    print("You lose!")
elif comp_choice < user_choice:
    print("You win!")
else:
    print("You lose!")
