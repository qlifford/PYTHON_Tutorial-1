# '''*******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/______/
# *******************************************************************************'''
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# choice1 = input("You're at a cross road. Where do you want to go? Type\n'L' for left or\n'R' for right:").upper()

# if choice1 == "l":
#     print("You've come to a lake. There is an island in the middle of the lake.")
#     choice2 = input("Type 'W' to wait or 'S' to swim").upper()
#     if choice2 == "w":
#         print("You waited for a boat and crossed the lake. You arrive at the island unharmed.")
#         choice3 = input("There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").upper()
#         if choice3 == "red":
#             print("It's a room full of fire. Game Over.")
#         elif choice3 == "yellow":
#             print("You found the treasure! You Win!")
#         elif choice3 == "blue":
#             print("You enter a room of beasts. Game Over.")
#         else:
#             print("You chose a door that doesn't exist. Game Over.")
#     else:
#         print("You got attacked by an angry trout. Game Over.")
        
        
        
        

print("Welcome to Treasure island.")
print("Your mission is to find the treasure.")
treasure = input("Left or Right?").lower()



if treasure =="left":
    process=input("swim or wait??")

    if process =="wait":
        print(" doors")

        door= input("Which door?(red or blue or yellow):").lower()

        if door=="red":
            print("Burnt by fire.\nGame over")

        elif door=="blue":
            print("Eaten by beasts\nGame over.")

        elif door == "yellow":
            print("You Win!")

        else:
            print("Game Over")

    else:
        print("Attacked by trouts.\nGame Over")
        
else:
    print("Fall into a hole.\nGame over")


