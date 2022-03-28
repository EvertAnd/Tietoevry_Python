# 1. What's the frequency?
# Write a function: get_char_count(text) that receives a string and returns a dictionary with the number of single letter applications.
# get_char_count ("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, '': 1}
# # dictionary sequence doesn't matter and the whole alphabet doesn't have to be included
#  There may also be a solution with Counter from standard Python library but this is definitely not necessary, although it is very elegant smile
#
print("UZD- 1.What's the frequency?")


def get_char_count(c):
    count = dict()
    c = str(input("Enter a text to count  letters:"))
    print(f"Count: " + c + "->")
    for i in c:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
print(get_char_count('c'))

# 2. Dictionary editor
# Write replace_dict_value (d, bad_val, good_val), which returns a dictionary with changed values
# The parameters of the function are the dictionary d to be processed and the values ​​bad_val to be changed to good_val
# clean_dict_value ({'a': 5, 'b': 6, 'c': 5}, 5, 10) -> {'a': 10, 'b': 6, 'c': 10}, because 5 was the value to be replaced.
#
print("UZD- 2.Dictionary editor")

def replace_dict_value(d, bad_val, good_val):
    for key, value in d.items():
        if value == bad_val:
            d[key] = good_val
    return d
my_dict = {'a': 5, 'b': 6, 'c': 5}
print(my_dict, "->", replace_dict_value(my_dict, 5, 10))


# 3. Dictionary cleaner
# 3a. Write clean_dict_value (d, bad_val), which returns a cleaned dictionary
# The parameters of the function are the dictionary d to be processed and the value bad_val to be disposed of together with its key.
# Example:
# clean_dict_value ({'a': 5, 'b': 6, 'c': 5}, 5) -> {'b': 6}, because 5 was a value for both a and c keys to get rid of.
# 3b Write clean_dict_values ​​(d, v_list), which returns a cleaned dictionary
# The parameters of the function are the dictionary d to be processed and the list of values ​​v_list to get rid of.
# clean_dict_values ​​({'a': 5, 'b': 6, 'c': 5, 'd':3}, [3,4,5]) -> {'b': 6} because 3 and 5 were in the list of values to delete.
# PS. Remember we can use del d ['a'] only if the key 'a' exists.
# !! When resizing a dictionary, we are not allowed to iterate at the same time!
# There are two options: either walk through the copy my_dict.copy.items (), or build a new dictionary. Dictionary comprehension would be one option.

print("UZD- 3.Dictionary cleaner")
