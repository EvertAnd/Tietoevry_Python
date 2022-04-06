# Day 13 - Work in Class
# Find a JSON API of your choice:
# A list of no authorization needed public JSON APIs:
# https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/
# Bigger JSON API list is here: https://github.com/public-apis/public-apis - but many require getting API key first - it may or may not be easy/fast.
# Write a Python program that accesses this API - (request library is fine),
# Ideally request is sent just 1 time, but up to 10 times is okay(with a little delay).
# Get 10 units of information (cats, dogs, beers, food items, jokes, etc) and extract information into Python data structure.
# Save data into an indented JSON text file (my_cats.json, etc) as an array of these data items.
# Bonus: filter some values/properties out, no need to completely copy everything.
# Bonus: allow user input to create some choice.
# Like what type of beers to look for, what dog breeds to find, what type of jokes to find, etc.
# An interesting API use can serve as start for your final project if you do not have one already.

import json
import requests

print("Find a JSON API of your choice")
print("This will get: Ron Swanson quotes.")
print("________________________________________________________")

getcount = int(input("How many quotes do you want to se: : "))


def get_Ron_Swanson_quotes(url=f'https://ron-swanson-quotes.herokuapp.com/v2/quotes/{getcount}'):
    requests.get(url)
    response = requests.get(url)
    data_from_json = response.json()
    with open("Quotes.json", mode="w") as write_file:
        json.dump(data_from_json, write_file, indent=4)

    return response


print(get_Ron_Swanson_quotes())
