print("Welcome to the Tip Calculator ! ")
bill = float(input("What was the total bill? $"))
Tip = int(input("How much Tip would you like to give?  10,12 or 15:"))
individual = int(input("Each individual should pay: "))

Total_bill = ((bill*Tip/100)+bill)/individual
print(Total_bill)