import random

# list of choice
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

# ask user for input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# computer choice
computer_choice = random.randint(0,2)

# 0 for tie, 1 for user win, 2 for computer win, -1 for invalid input
win_or_lose = 0

# check if the input is between 0-2
if user_choice > 2 or user_choice < 0:
    win_or_lose = -1
else:
    # print out the ascii art
    print(choices[user_choice])
    print("Computer chose:")
    print(choices[computer_choice])

    # determine who win the game
    if user_choice == 0:
        if computer_choice == 1:
            win_or_lose = 2
        if computer_choice == 2:
            win_or_lose = 1
    if user_choice == 1:
        if computer_choice == 0:
            win_or_lose = 1
        if computer_choice == 2:
            win_or_lose = 2
    if user_choice == 2:
        if computer_choice == 0:
            win_or_lose = 2
        if computer_choice == 1:
            win_or_lose = 1

# base on win or lose flag print out the result
if win_or_lose == 1:
    print("You win!")
elif win_or_lose == 2:
    print("You lose!")
elif win_or_lose == 0:
    print("It's a tie!")
else:
    print("You lose! You choose a number that's not between 0-2.")
    