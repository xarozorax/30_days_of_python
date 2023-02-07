__name__ = 'geometry'

# This should be a collection of pure functions for geometric purposes of this day's assignments
# All functions assume that their input data is well-formatted and appropriate for the use-case
# This will be enforced by error-handling in the calling files


# Imports


import math


# Constants


PI = 3.14

# Functions


def tri_area(b, h):
    return b * h * 0.5


def poly_perimeter(*args):
    return sum(args)


def rect_area(l, w):
    return l * w


def rect_perimeter(l, w):
    return 2 * l + 2 * w


def circ_area(rad):
    return PI * rad ** 2


def circ_circum(rad):
    return PI * rad * 2


def slope_from_points(point_1, point_2):
    delta_x: float = point_2[0] - point_1[0]
    delta_y: float = point_2[1] - point_1[1]
    return delta_x / delta_y


def euclid_dist(point_1, point_2):
    delta_x: float = point_2[0] - point_1[0]
    delta_y: float = point_2[1] - point_1[1]
    return math.sqrt(delta_x ** 2 + delta_y ** 2)

