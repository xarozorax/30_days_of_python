# Imports

import geometry.geometry as geo


# 'Non-script' assignments


# Tasks 1 - 3

age = 27
height = 69.5
complex_num = 2 + 5j


# Tasks 6 - 20

# 6

def ui_rect_area_perimeter():
    try:
        side_1 = float(input('Input length of side one - '))
        side_2 = float(input('Input length of side two - '))
        area = geo.rect_area(side_1, side_2)
        perim = geo.rect_perimeter(side_1, side_2)
        print(f'The rectangle\'s area is {area} and perimeter is {perim}.')
    except ValueError:
        print('Please input either integer or decimal numbers.')
        ui_rect_area_perimeter()


# 7

def ui_circle_area_circum():
    try:
        rad = float(input('Input radius of circle - '))
        area = geo.circ_area(rad)
        circum = geo.circ_circum(rad)
        print(f'The circle\'s area is {area} and circumference is {circum}')
    except ValueError:
        print('Please input either integer or decimal numbers.')
        ui_circle_area_circum()


# 8

'''
This particular problem is a bit... goofy. The prompt is 'Calculate the slope, x-intercept and y-intercept of y = 2x -2'
The strangeness of the prompt comes from the nature of the form that the equation was given in
y=2x-2 is in Slope-Intercept form, which is y=mx+b
This form of equation gives the slope and y-intercept as a parts of the equation
Slope == m, y-intercept == (0, b)
The only 'calculable' part is the x-intercept, which == ((0=2x-2), 0)

As a result, I'm going to skip this prompt.
'''


# 9

def ui_slope_euclid_dist():
    print('Please enter points in the form of (x, y) or (x,y)')
    point_1_in = input('Please enter point one - ')
    point_2_in = input('Please enter point two - ')
    try:
        point_1_strs = point_1_in.replace('(', '').replace(')', '').replace(' ', '').split(',')
        point_2_strs = point_2_in.replace('(', '').replace(')', '').replace(' ', '').split(',')
        point_1 = []
        point_2 = []
        for i in point_1_strs:
            point_1.append((float(i)))
        for i in point_2_strs:
            point_2.append((float(i)))
        slope = geo.slope_from_points(point_1, point_2)
        dist = geo.euclid_dist(point_1, point_2)
        print(f'The slope between the points is {slope} and the euclidean distance is {dist}')
    except ValueError:
        print(
            '''
            I actually still need to figure out what exactly will cause a ValueError here, but please
            allow this for the foreseeable future
            '''
        )
        ui_slope_euclid_dist()
    except TypeError:
        print(
            '''
            I also need to figure out what will throw a TypeError
            '''
        )
        ui_slope_euclid_dist()
    except Exception as e:
        print(
            '''
            I really haven't figure out what will cause any other errors here, so we'll go ahead and leave this 
            open for interpretation... and SCIENCE!
            ''', str(e)
        )


# ui_slope_euclid_dist()


# 10
# Compare slopes of tasks 8 and 9

def ui_compare_two_nums():
    try:
        one = float(input('Please enter number one - '))
        two = float(input('Please enter number two - '))
        if one > two:
            print('Num one is greater than num two')
        elif two > one:
            print('Num two is greater than num one')
        else:
            print('The numbers are equal')
    except ValueError:
        print('Please enter two integers or decimal numbers')
        ui_compare_two_nums()


# ui_compare_two_nums()


# 11


# y=x^2+6x+9
# Use multiple x values to find y==0


def parabolic_y():
    for x in range(-10, 10):
        print(x ** 2 + 6 * x + 9)
        if x ** 2 + 6 * x + 9 == 0:
            print(f'For x^2+6x+9, the x intercept is ({x}, 0)')

# parabolic_y()


# 12

# length of 'dragon' and 'python'; falsy comparison

falsy_length = len('dragon') != len('python')
# print(falsy_length) # 'False'

# 13

# use AND to check if 'on' in both 'python' and 'dragon'

on_in_both = 'on' in 'python' and 'on' in 'dragon'
# print(on_in_both) # 'True'


# 14

# 'I hope this course is not full of jargon' - check if 'jargon' in sentence

def jargon_in_sentence():
    return 'jargon' in 'I hope this course is not full of jargon'

# print(jargon_in_sentence())


# 15

# no 'on' in both 'python' and 'dragon'

def no_on_in_both():
    return 'on' not in 'python' and 'on' not in 'dragon'


# 16

# print(no_on_in_both())

python_length = str(float(len('python')))


# 17

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# 18

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

floor_thing = 7 // 3 == int(2.7)

# print(floor_thing)


# 19

# Check if type of '10' is equal to type of 10

num_not_string = type(10) == type('10')

# print(num_not_string)


# 20

# Check if int('9.8') is equal to 10

'''
See example 19, lines 202-207
'''
