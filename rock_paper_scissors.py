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

#code for rock paper scissors
a = [0,1,2]
game_images= [rock, paper, scissors]
user_choice = int(input("enter your choice from 0, 1 or 2: "))
computer_choice = random.choice(a)

print(game_images[computer_choice])

if user_choice>=3 or user_choice < 0:
  print("invalid user value, YOU LOOSE!")
else:
  print(game_images[user_choice])


if computer_choice == 2 and  user_choice == 0:
  print("YOU WIN")
elif computer_choice == 0 and user_choice == 2:
  print("YOU LOOSE")
elif computer_choice == user_choice:
  print("YOU LOOSE, It's a draw!")
elif computer_choice > user_choice:
  print("YOU LOOSE")
elif user_choice > computer_choice:
  print("YOU WIN")
else: 
  print("INVALID!")
