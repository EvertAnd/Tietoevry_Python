# 1. FizzBuzz
# Print a string 1,2,3,4, Fizz, 6, Buzz, 8, ..... 34, FizzBuzz, 36, .... to 97, Buzz, 99, Fizz
# So if number divided by 5 then Fizz If divided by 7 then Buzz, If divided by 5 AND 7 then FizzBuzz otherwise the same number
#  Note: such a task became popular as the first task to ask to determine whether a person knows about programming at all smile

Fizz = 5
Buzz = 7
start = 1
the_end = 100
# for n in range(start, the_end):
#     print(n,end="")
for n in range(start, the_end):

    if n == the_end:
        if n % (Fizz*Buzz) == 0:
            print("FizzBuzz", end="")
    if n % Fizz == 0:
        print("Fizz",end="")
    if n % Buzz == 0:
        print("Buzz", end="")
    else:
        print(n, end=" ")


#
#
#
#  2. Christmas tree
# Enter the height of the tree
# Print the tree: Ex. height == 3
# The printout would be:
#   *
#  ***
# *****
# Note: remember that several symbols can be printed at once, for example: print ("" * 10 + "*" * 6)

# height = int(input("Cik garu eglīti gribi?: "))
# for i in range(height):
#     print(' ' * (height - i - 1) + '*' * (2 * i + 1))  # x2 is always rounded up


#
# 3. Primes Check if entered positive number is a prime number.
#  A prime number is a number that divides without remainder only by itself and 1.
# Hint: what numbers do we have to check?