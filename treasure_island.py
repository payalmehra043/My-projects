print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
******************************************************************************* ''')
print("Welcome to Treasure Island!")
print("Your Mission is to find the Treasure.")
print('You are at a road. Where do you want to go?'
           'Type "left" or "Right".') 
choice1 = input("")
if choice1 == "left":
      print("You have to come a lake.There is an island in the middle of the lake.") 
      print('Type "wait" for boat. Type "swim" to swim across')
      lake = input("")        
      if lake == "wait":
          print("You arrive at the Island unharmed.There is a house with three doors.one red,one yellow and one blue.")
          print('Which colour do you want to choose?')
          Door =input("") 
          if  Door == "yellow":
               print("You found the treasure! Congratulations!")
          elif Door =="red":
               print("it's room full of fire.Game Over")
          elif Door == "blue":
               print("you enter a room of beasts.Game Over")
          else:
               print("You choose a door which does not exist.Game over")
      elif lake == "swim":
               print("You got crocodile attacked. Game over!")

else:
    print("You fell into a hole. Game Over")
