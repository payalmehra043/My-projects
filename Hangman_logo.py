import random


logo = r'''              
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/         '''
 

print(logo)
lives = 6
words_list = ["wait","queue","ready"]
choosen_word = random.choice(words_list)
print(choosen_word)

place_holder = ""
word_length = len(choosen_word)
for position in range(word_length):
    place_holder += "_"
print(place_holder)
game_over = False
correct_letter = []

while not game_over:
   
   guess = input ("Guess a letter:").lower()
   print(guess)
   display = ""

   for letter in choosen_word:
      if letter == guess:
        display += letter
        correct_letter.append(guess)

      elif letter in correct_letter:
        display += letter
      else:
        display += "_"
   print(display) 



   if guess not in choosen_word:
        lives -= 1
        if lives == 0:
          game_over = ("you lose.")


    

   if "_" not in display:
        game_over = True
        print("you win.")

   print(logo[lives])