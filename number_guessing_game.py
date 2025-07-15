import random


print("Welcome to our number guessing game!")
while True:
    answer = input("Continue?: ").lower()
    if not answer.startswith('y'):
        print("Invalid input!")
        continue   
    num = int(input("Enter a range: "))
    random_number = random.randrange(1, num)
    while True:
        my_guess = int(input("Make a guess: "))
        if my_guess > num:
            print("Sorry... Your guess is out of range!")
        elif my_guess < 1:
            print(f"Sorry... Guess must be between 1 and {num}!")
        elif my_guess > random_number:
            print("Sorry.. Your guess was above the number!")
        elif my_guess < random_number:
            print("Sorry.. Your guess was below the number!")
        elif my_guess == random_number:
            print("✅✅... You guessed it right!")
            print("Game over!")
            quit()
            break
        else:
            print("Quit")
        # continue
