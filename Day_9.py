# 1. Min, Avg, Max
# Write a function get_min_avg_max (sequence) that returns a tuple with three values, the smallest, the arithmetic mean,
# and the largest value in the string, respectively.
# Example:
# get_min_avg_max ([0,10,1,9]) -> (0,5,10)
# the incoming sequence can be a tuple or a list with numeric values.
#
print("UZD- 1.Min, Avg, Max")

def get_min_avg_max(value_list):
    print(value_list)
    avg = sum(value_list) / len(value_list)
    return min(value_list), int(avg), max(value_list)

print(get_min_avg_max([0, 10, 1, 9]))

# 1b for those more experienced
# Write a function get_min_med_max (sequence) that returns a tuple with three values, the smallest, the median, and the largest value from the string, respectively.
#
# The median value is the value that is in the middle of the sequence. If the number of strings is even then there are two values ​​in the middle.
# https://en.wikipedia.org/wiki/Median
# get_min_med_max ([1,5,8,4,3]) -> (1,4,8)
# get_min_med_max ([2,2,9,9,4,3]) -> (2,3.5,9)
# get_min_med_max ("baaac") -> ('a', 'a', 'c')
#  # with a string input we can have interesting results at an even number having an average, so it's better to give both averages
# get_min_med_max ("faaacb") -> ('a', 'ab', 'f')
# the incoming sequence can be a tuple or list with values ​​of the same type, or even a string.
#
print("UZD- 1.Min, med, Max")
def get_min_med_max(value_list):

    sorted_l = sorted(value_list)
    med_index = len(sorted_l) / 2

    if not med_index % 1 == 0:
        med_index = int((len(sorted_l) - 1) / 2)
        med = sorted_l[med_index]
    else:
        if type(sorted_l[int(med_index) - 1]) is str:
            med = sorted_l[int(med_index) - 1] + sorted_l[int(med_index)]
        else:
            med = (sorted_l[int(med_index) - 1] + sorted_l[int(med_index)]) / 2

    return min(value_list), med, max(value_list)

# get_min_med_max ([1,5,8,4,3]) -> (1,4,8)
# get_min_med_max ([2,2,9,9,4,3]) -> (2,3.5,9)
# get_min_med_max ("baaac") -> ('a', 'a', 'c')
# get_min_med_max ("faaacb") -> ('a', 'ab', 'f')
print(get_min_med_max ([1,5,8,4,3]))
print(get_min_med_max ([2,2,9,9,4,3]))
print(get_min_med_max ("baaac"))
print(get_min_med_max ("faaacb"))



# 2. Common Elements
# Write a function that returns a tuple with common elements in three sequences. Inputs can be list, tuple, string.
# get_common_elements (seq1, seq2, seq3)
# Example:
# get_common_elements ("abc", ['a', 'b'], ('b', 'c')) -> ('b',) # we return a tuple with a single element
# # remember that we can convert strings to set with set(mystring), and set to tuple with tuple(myset)
# 2. b For those with some experience
# BONUS:  make a function that can handle an arbitrary number of input sequences
# 3. Is there a pangram?
# Write a function is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz')
# that returns True when the text parameter contains all the letters passed in an alphabet.
# We return False otherwise
# pangram - sentence, word string containing all letters of the alphabet - https://en.wikipedia.org/wiki/Pangram
# We ignore spaces and believe that uppercase is as valid as lowercase, i. here A and a -> a
# print(is_pangram("The five boxing wizards jump quickly")) -> True
# print(is_pangram("Not a pangram")) -> False
# Bonus: test it also on Latvian alphabet:
# a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'
# print(is_pangram('Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!', alphabet=a_lv)) -> True
