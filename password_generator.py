letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['@','_','!','$','*','&','#']

print("Welcome to pypassword generator!")
nr_letter =int( input("How many letters do you want to set in your password?\n"))
nr_numbers = int(input("How many numbers do you want to set in your password?\n"))
nr_symbols = int(input("How many symbols do you want to set in your password?\n"))
#import random
#password = " "

#for char in range(0,nr_letter):
    #password += random.choice(letters)
   

#for char in range(0,nr_numbers):
    #password += random.choice(numbers)
    
#for str in range (0,nr_symbols):
    #password += random.choice(symbols)


#print(password)

#another way 
import random
password_list = []
for char in range(0,nr_letter):
    password_list.append(random.choice(letters))

for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))


print(password_list)
random.shuffle(password_list)
print(password_list)


password = ""
for char in password_list:
    password += char
print(f"Your password  is {password}")























