# using choice function
import random

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
---'   ____)____
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

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")
)

if 0 <= user_choice <= 2:
    choices = [rock, paper, scissors]
    print(choices[user_choice])

    computer_choice = random.choice(choices)
    print("Computer chose:\n", computer_choice)

    if (
        (user_choice == 0 and computer_choice == scissors)
        or (user_choice == 1 and computer_choice == rock)
        or (user_choice == 2 and computer_choice == paper)
    ):
        print("You won!")
    elif (
        (user_choice == 0 and computer_choice == paper)
        or (user_choice == 1 and computer_choice == scissors)
        or (user_choice == 2 and computer_choice == rock)
    ):
        print("You lose!")
    elif (
        (user_choice == 0 and computer_choice == rock)
        or (user_choice == 1 and computer_choice == paper)
        or (user_choice == 2 and computer_choice == scissors)
    ):
        print("It's a Draw!")
else:
    print("You typed an invalid number, you lose!")

print("_\n")
