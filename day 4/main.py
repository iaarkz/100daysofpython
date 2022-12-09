import random

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

game_choice = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0: 
  print("Print a valid number between 0 and 2.")
else: 
  print(game_choice[user_choice])

  pc_choice = random.randint(0,2)
  print("Computer chose:")
  print(game_choice[pc_choice])

  if user_choice == 0 and pc_choice == 0:
    print("Draw!")
  elif user_choice == 0 and pc_choice == 1:
    print("You lose!")
  elif user_choice == 0 and pc_choice == 2:
    print("You won!")
  elif user_choice == 1 and pc_choice == 0:
    print("You won!")
  elif user_choice == 1 and pc_choice == 1:
    print("Draw!")
  elif user_choice == 1 and pc_choice == 2:
    print("You lose!")
  elif user_choice == 2 and pc_choice == 0:
    print("You lose!")
  elif user_choice == 1 and pc_choice == 1:
    print("You won!")
  elif user_choice == 1 and pc_choice == 3:
    print("Draw, play again.")
