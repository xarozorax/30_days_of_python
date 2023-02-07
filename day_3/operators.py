__name__ = 'day_3_operators'

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
