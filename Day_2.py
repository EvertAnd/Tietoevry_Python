# Day 2 - Work in Class
# 1. Exercise - Age 100

# Write a program that asks for and saves a username                                         ok
# Ask a question about the user's age, using the username in the question.                    ok
# Shows in how many years the user will be 100 years old smile                                ok
# BONUS: Let the program also show the year when the user will be 100 years old.              ok
# It could use a variable with the current year.
# It would be even better to get the current year automatically
# then you will need two additional lines:
# import datetime # let's talk about imports separately
# currentYear = datetime.datetime.now (). year

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
# 2. Exercise - Room volume
#
# Ask user to input 3 numbers - width, length, height
# Find the volume of the room
# PS Think about units and what is the most appropriate data type for this
width = float(input("Ievadi istabas platumu"))
length = float(input("Ievadi istabas garumu"))
height = float(input("Ievadi istabas augstumu"))
room_vol = width * length * height
print(f"Istabas kubatūra ir {room_vol} m\u00b3")

#_______________________________________3.uzdevums____________________________________

# 3. Exercise - Temperature Conversion
#
# Write a program that asks user for temperature in Celsius and prints out this same temperature in Farenheit
# formula is: farenheit = 32+celsius*(9/5)
# PS Remember about data type conversion, also consider precision

Tmp_C = float(input("Ievadi  temperatūru C un es to pārveidošu un Farenheitiem"))
Tmp_f = 32 + Tmp_C * (9 / 5)
Tmp_f_Round = round(Tmp_f, 2)   #pieliku skatoties risinājumus
print(f"Šī temperatura pēc Farenketa skalas būs {Tmp_f}")

#_____________________________________Rezultāts_______________________________

# Kā tevi sauc mans draugs?Andis
# Andis cik tev ir gadi?36
# Jauki, tad tu pēc 64 būsi jau 100 gadus vecs :)
# Un 2058. gadā tu būsi tieši 100 gadus vecs!
# Ievadi istabas platumu23.5
# Ievadi istabas garumu34
# Ievadi istabas augstumu3.5
# Istabas kubatūra ir 2796.5 m³
# Ievadi  temperatūru C un es to pārveidošu un Farenheitiem31
# Šī temperatura pēc Farenketa skalas būs 87.80000000000001
#
# Process finished with exit code 0