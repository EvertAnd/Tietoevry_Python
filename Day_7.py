# 1. The Big Result
#
# Write an add_mult function that requires three parameters / arguments
# Returns the result that is the sum of the 2 smallest arguments multiplied by the largest argument value.
# PS Assume that numeric parameters will always be passed to the function, no need to check types
# Various solutions are possible (you are allowed to use other data structures inside function such as list).
# Example add_mult (2,5,4) -> will return (2 + 4) * 5 = 30


def add_mult(a, b, c):
    a, b, c = sorted([a, b, c])
    # print([a], [b], [c])
    print(f"will return  ({a}+{c})*{b}")
    return (a + b) * c


my_result = add_mult(2, 5, 4)
print(my_result)

#
# 2. Palindrome
#
# Write the function is_palindrome (text)
# which returns a bool True or False depending on whether the word or sentence is read equally from both sides.
# PS You can start with a one-word solution from the beginning, but the full solution will ignore whitespace and uppercase and lowercase letters.
#
# is_palindrome ("Alus ari i ra    sula") -> True
# is_palindrome("ABa") -> True
# is_palindrome("nava") -> False
#

def is_palindrome(text):
    reversed_text = text[::-1]
    return text == reversed_text
while True:
    txt = str(input("Enter a text to see if it is a palindrome or not:"))
    if txt.lower() == 'q':
        print("Thank you! Exiting")
        break
    else:
        output = " a palindrome!" if is_palindrome(txt) else " NOT a polindrome!"
        print(f"Your text -> {txt} is  {output}")

# 3. City Population
#
# The city has a known population p0
# A percentage of population perc is added each year
# Every year a certain number of delta also arrive (or leave)
# We need to know when (if at all) the city will reach a population of p
# Write a function get_city_year (p0, perc, delta, p) that returns the years (full) when p is reached.
#
# If p cannot be reached, then we return -1
#
# Example:
#
# get_city_year (1000,2,50,1200) -> 3
# 1000 + 1000 * 0.02 + 50 => 1070 after the 1st year
# 1070 + 1070 * 0.02 + 50 => 1141 after the 2nd year
# 1141 + 1141 * 0.02 + 50 => 1213 after the 3rd year
# so the function here returns 3 and is done
#
# PS. Note that we give perc as a percentage to be converted to a decimal number.
#
#
#
# More test examples:
#
# get_city_year (1000, 2, -50, 5000) -> -1
# get_city_year (1500, 5, 100, 5000) -> 15
# get_city_year (1500000, 2.5, 10000, 2,000,000) -> 10
# Submission status
