# Imports


# Day 4 of 30 Days of Python


# 1
# Concatenate strings 'Thirty', 'Days', 'Of', 'Python' for string 'Thirty Days Of Python'
# Prompt does not say to display the resultant string, nor to return it


def tdop_concat():

    strings = ('Thirty', 'Days', 'Of', 'Python')
    output = ""
    for word in strings:
        output = output + word + " "


# 2
# Concatenate strings 'Coding', 'For', 'All' for string 'Coding For All'
# This was as many times as I was willing to do this prompt before refactoring it to its own function that accepted
# a list of strings


def cfa_concat():

    strings = ('Coding', 'For', 'All')
    output = ""
    for word in strings:
        output = output + word + " "


# 3
#