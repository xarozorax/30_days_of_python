# Day 2: 30 Days of python programming

# Cheat a bit, and don't necessarily make just the vars = makes it easier in later portions
# Also, I'm counting it as declaring 'all' of the vars on one line

import math

attributes = {
    'first_name': 'Bobb',
    'last_name': 'Harris',
    'full_name': 'Bobb Harris',
    'country': 'USA',
    'city': 'SLC',
    'age': 27,
    'year': 1995,
    'is_married': False,
    'is_true': True,
    'is_light_on': True
}

# Check the types of all vars in dict.attributes

for attr in attributes:
    print(attr + ' is ' + str(attributes[attr]))

# Name length stuff

name_lengths = (len(attributes['first_name']), len(attributes['last_name']))

# Print first_name.len, then comparison of first_name.len vs last_name.len

print(str(name_lengths[0])+"\n")
print('My last name is longer than my first name by ' + str(name_lengths[1]-name_lengths[0]))

# Maths stuff
# Only told to store values in vars, not going to print anything!

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# Radius stuff

r30 = 30


def area_of_circle(rad):
    return math.pi * (rad ** 2)

# Calculate area of radius 30 circle


v_area_of_circle = area_of_circle(r30)


circum_of_circle = 2 * math.pi * r30


def ui_circle_area():
    rad = input('Please input a radius to calculate the area of a circle - ')
    try:
        rad = float(rad)
        area_of_circle(rad)
    except TypeError:
        print('Please input a number, either integer or decimal.')
        ui_circle_area()


ui_circle_area()

for attr in attributes:
    if attr in {'first_name', 'last_name', 'country', 'age'}:
        attributes[attr] = input(f'Please enter your {attr} - ')
    else:
        pass
