# Day 2 - Work in Class
# 1. Exercise - Age 100
#
# Write a program that asks for and saves a username                                         ok
# Ask a question about the user's age, using the username in the question.                    ok
# Shows in how many years the user will be 100 years old smile                                ok
# BONUS: Let the program also show the year when the user will be 100 years old.
# It could use a variable with the current year.
# It would be even better to get the current year automatically
# then you will need two additional lines:
# import datetime # let's talk about imports separately
# currentYear = datetime.datetime.now (). year
# 2. Exercise - Room volume
#
# Ask user to input 3 numbers - width, length, height
# Find the volume of the room
# PS Think about units and what is the most appropriate data type for this
# 3. Exercise - Temperature Conversion
#
# Write a program that asks user for temperature in Celsius and prints out this same temperature in Farenheit
# formula is: farenheit = 32+celsius*(9/5)
# PS Remember about data type conversion, also consider precision

#_______________________________________1.uzdevums____________________________________
import datetime

my_name = input("Kā tevi sauc mans draugs?")
my_age = int(input(f"{my_name} cik tev ir gadi?"))
old_age = 100
till_old = old_age-my_age
curr_date = datetime.datetime.now().year
old_age_after =curr_date + my_age
print(f"Jauki, tad tu pēc {till_old} būsi jau 100 gadus vecs :)")
#Bonuss
print(f"Un {old_age_after}. gadā tu būsi tieši 100 gadus vecs!")

#_______________________________________2.uzdevums____________________________________