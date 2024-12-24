

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