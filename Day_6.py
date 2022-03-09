# 1a. Average value
# Write a program that prompts the user to enter numbers (float).
# The program shows the average value of all entered numbers after each entry.
# PS. 1a can do without a list
# 1b. The program shows both the average value of the numbers and ALL the numbers entered
# PS Exit the program  by entering "q"
# 1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.
print("1.Uzd_Vidējais starp skaitļiem")
numbers = input("Ievadi numurus katru atdalot ar "+'","'+"q-lai izzietu"+":")
if numbers == "q":
    print("You decided to quit")
else:
    number_list = numbers.split(",")
    sum = 0
    for n in number_list:
        sum += float(n.strip())
    average = sum / len(number_list)
print("1b. The program shows both the average value of the numbers and ALL the numbers entered")
print(f"{average} šis ir vidējais skaitlis")
print(f"Tevis ievadītie skaitļi: {number_list}")
print("1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.")
print(f"Augšējie 3 {sorted(number_list)[:3]}")
print(f"Apakšējie 3 {sorted(number_list)[-3:]}")
print(f"{average} šis ir vidējais skaitlis")

# 2. Cubes
# The user enters the beginning (integer) and end number.
# The output is the entered numbers and their cubes
# For example: inputs 2 and 5 (two inputs)
# Output
# 2 cubed: 8
# 3 cubed: 27
# 4 cubed: 64
# 5 cubed: 125
# All cubes: [8,27,64,125]
# PS could theoretically do without a list, but with a list it will be more convenient
print("2.Uzd_Kubs_Ievadi divus skaitļus pirmo mazāku otro lielāku")
a = int(input("Pirmais skaitlis: "))
b = int(input("Pēdējais skaitlis: "))
list = []
for n in range(a, b+1):
    cube = n**3
    print(f"{n} cubed: {cube}")
    list.append(cube)
print(list)

# 3. Reversed words
# The user enters a sentence.
# We output all the words of the sentence in reverse form. - not the whole text reversed!!
# Example
# Alus kauss mans -> Sula ssuak snam
# PS Split and join operations could be useful here.
print("3.Uzd_Apgrieztie vārdi")
teikums = input("Ievadi teikumu: ")
vardi = teikums.split()
print(vardi)
reversed_v = [v[::-1] for v in vardi]
print(reversed_v)
reversed_t = ' '.join(reversed_v)
print(f"{teikums} -> {reversed_t}")



# 4. Prime numbers -
# this could be a weekend assignment, there is hardly enough time in class
# Find and output the first 20 (even better option to choose how many first primes we want) prime numbers in the form of a list i.e. [2,3,5,7,11, ...]