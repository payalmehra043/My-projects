rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock,paper,scissors]
user_choice =int(input("What do you choose?Type 0 for rock,1 for paper or 2for scissors\n"))
print(game_images[user_choice])
import random
computer_choice = random.randint(a=0,b=2)
print("computer choose.")
print(game_images[computer_choice])
if  user_choice > 3 or user_choice < 0:
    print("Invalid input")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice== 0 and user_choice == 2:
    print("you lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")

elif computer_choice == user_choice:
    print("It's a tie!")

else :
     print("you typed invalid no.you lose!")