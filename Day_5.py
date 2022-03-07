# 1. Confusion
# The user enters a name.
# You print user name in reverse (should begin with capital letter) then extra text: ",a thorough mess is it not ", then the first name of the user name then "?"
# Example:
# Enter: Valdis -> Output: Sidlav, a thorough mess is it not V?
#

print("______________________1. UZDEVUMS __________________________")

vards = input(print("Ievadi savu vārdu"))
r_vards = vards[::-1]
print(f"Sveiks {vards[:-1]} Tavs vārds apgriestā veidā būtu: " + r_vards.capitalize())


# 2. Almost Hangman
# Write a program to recognize a text symbol
# The user (first player) enters the text.
# Only asterisks instead of letters are output.
# Assume that there are no numbers, but there may be spaces.
# The user (i.e. the other player) enters the symbol.
# If the letter is found, then the letter is displayed in ALL the appropriate places, all other letters remain asterisks.
# Example:
#
# First input: Kartupeļu lauks -> ********* *****
# Second input: a -> *a****** *a***
#
# In principle, this is a good start to the game of hangman.
# https://en.wikipedia.org/wiki/Hangman_(game)
#
# 3. Text conversion
#
# Write a program for text conversion
# Save user input
# Print the entered text without changes
# Exception: if the words in the input are not .... bad, then the output is not ...  bad section must be changed to is good
#
# Examples:
#
# The weather is not bad -> The weather is good
# The car is not new -> The car is not new
# This cottage cheese is not so bad -> This cottage cheese is good
# Hints:
# Find (or index, or even rfind) will probably come in handy, as may an operator. Also slice syntax will be useful.
# Extra: How would you do this task in Latvian language (nav slikts/a -> ir labs/a)?