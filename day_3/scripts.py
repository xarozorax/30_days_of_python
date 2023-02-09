import geometry.geometry as geo

'''
I guess most of the examples in operators.py are 'scripts,' but this will have to do...
'''

# 4

# Write a script that prompts the user to enter base and height
# of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

def get_tri_area():
    try:
        base = float(input('Please enter the base dimension - '))
        height = float(input('Please enter the height dimension - '))
        return geo.tri_area(base, height)
    except ValueError:
        print('Please input an integer or decimal number')
        get_tri_area()


# 5

# Write a script that prompts the user to enter side a, side b, and side
# c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

def get_tri_perim():
    try:
        side_1 = float(input('Please enter length of side one - '))
        side_2 = float(input('Please enter length of side two - '))
        side_3 = float(input('Please enter length of side three - '))
        return sum(side_1, side_2, side_3)
    except ValueError:
        print('Please input an integer or decimal number')
        get_tri_perim()


# 21

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

def pay_calc():
    try:
        wage = float(input('Input wage of employee - '))
        hours = float(input('Input hours of employee - '))
        return wage * hours
    except ValueError:
        print('Please enter an integer or decimal number')
        pay_calc()


# 22

# Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live. Assume a person can live hundred years

def secs_in_years():
    try:
        years = float(input('How many years would you like to translate to seconds? - '))

        # seconds = years * 365.24 days/year * 24 hours/day * 60 minutes/hour * 60 seconds/minute

        return 60 * 60 * 24 * 365.24 * years


# 23

# Write a Python script that displays the following table

'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''
