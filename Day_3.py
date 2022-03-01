# ___________________________________Day 3 - Logic, Branching Class Exercises

print(" 1. Weselības pārbaude")
# Ask user for their temperature.
# If the user enters below 35, then output "not too cold"
# If 35 to 37 (inclusive), output "all right"
# If the temperature  over 37, then output  "possible fever"

Health_temp = float(input("Kāda ir tava pašreizējā ķermeņa temperatura? : "))
if Health_temp < 35:
    print("Temperatūra ir par zemu")
elif Health_temp <=37:
    print("Temperatūra normas robežās")
else:
    print("Pārāk liela temperatūra, iespējams drudzis")


print(" 1. Ziemassvētku bonuss")
# The company has promised a Christmas bonus in the amount of 15% of the monthly salary for EVERY year of service over 2 years.
# Task. Ask the user for the amount of the monthly salary and the number of years worked.
# Calculate the bonus.
# Example1: 5 years of experience, 1000 Euro salary, the bonus will be 450 Euro.
# Example2: 1.5 years of experience, 1500 Euro salary, no bonus(0).

precision = 2
bonus = 0.15
min_service_time = 2

wage = float(input("Kāda ir tava mēnešalga?"))
expierence = float(input("Kāds ir tavs darba stāžs"))

if expierence > precision:
    bonus_ammount = round((expierence - min_service_time)*bonus*wage, 2)
    print(f"Tava darba pieredze ir {expierence} gadi tāpēc bonusā saņemsi {bonus_ammount} Euro ")
else:
    print("Diemžēl darba stāžs ir par zemu un šoreiz bonus nepienākas")


print("3. Sakārto ievadīto skaitļus")

# Ask the user to enter 3 numbers, output them in ascending order.
# Note: for now, we solve this task only with if, elif, else actions.
# There is also a solution using sorting and list structure, which we have not yet seen.

a = float(input("Ievadi pirmo skaitli"))
b = float(input("Ievadi pirmo skaitli"))
c = float(input("Ievadi pirmo skaitli"))

numbers = [a,b,c]                     # pŗāk ilgi domāt loģiku sakārtot :D tāpēc kārtoju  sarakstu uzreiz.
numbers_sorted = sorted(numbers)
print(numbers_sorted)