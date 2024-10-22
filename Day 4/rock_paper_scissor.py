import random

#ASCII art for each move in the game
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print("Welcome to Rock Paper Scissor.")

#Ensure User enters a valid integer
while True:
    #Prompt user to enter a choice for the game
    user_choice = int(input("Please enter 0 for rock, 1 for paper, or 2 for scissors."))

    if user_choice > 2 or user_choice < 0:
        print("Invalid Number Try Again.")
    else:
        break

#Print out users choice move
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)



#Have computer choose randomly choose game option
computer_choice = random.randint(0,2)

print(f"Computer chose: ")

#Print out computers choice move
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)


#Compare results
if computer_choice == user_choice:
    print("Tie Game!")
elif computer_choice == 0 and user_choice == 1:
    print("You Win the Game!")
elif computer_choice == 1 and user_choice == 2:
    print("You Win the Game!")
elif computer_choice == 2 and user_choice == 0:
    print("You Win the Game!")
elif computer_choice == 1 and user_choice == 0:
    print("You Lose!")
elif computer_choice == 2 and user_choice == 1:
    print("You Lose!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose!")





