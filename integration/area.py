import math


def calculate_area_of_triangle(a, b, c):

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area