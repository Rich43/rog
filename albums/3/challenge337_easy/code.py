'''
This challenge is about finding minimums/maximums.
The challenge consists of two similar word problems where you will be
asked to maximize/minimize a target value.

To make this more of a programming challenge rather than using
programming as a calculator, I encourage you to try to find a generic
minimize/maximize function rather than just calculating the answer directly.
Challenge

A piece of wire 100 cm in length is bent into the shape of a sector
of a circle. Find the angle of the sector that maximizes the area A of
the sector. sector_image

A and B are towns 20km and 30km from a straight stretch of river 100km long.
Water is pumped from a point P on the river by pipelines to both towns.
Where should P be located to minimize the total length of pipe AP + PB? river_image

Challenge Outputs

The accuracy of these answers will depending how much precision you use when calculating them.

    ~114.6
    ~40

'''
import math


def radius(p, a):
    ''' int, int -> float
    find radius from the
    perimeter '''

    r = p / (((2 * math.pi * a) / 360) + 2)
    return r

def area(r, a):
    ''' int, int -> float
    find the area of a segment
    of a circle '''

    the_area = (a * math.pi /360) * r ** 2
    return the_area


''' The tactic is to search from 1 degree to 180 degrees while
varying the radius to find the perimeter of 100, once found 
checking the area size, and comparing to find the maximum area '''

P = 100
relevant_angle = 0
max_area = 0

for angle in range(1,181):
    # find the radius of the angle to give a perimrter of 100 cm
    the_radius = radius(P, angle)

    the_area = area(the_radius, angle)

    if the_area > max_area:
        max_area = the_area
        # keep a record of the angle
        relevant_angle = angle

# This gives an approximate of 115 degrees so will search from
# 114 to 116 degrees in 0.01 steps.

angle = relevant_angle
ans = 0

for angle in range((angle -1) * 1000, (angle + 2) * 1000, 1):
    angle = angle / 1000

    # find the radius of the angle to give a perimeter of 100 cm
    the_radius = radius(P, angle)

    the_area = area(the_radius, angle)

    if the_area > max_area:
        max_area = the_area
        # keep a record of the angle at max area
        relevant_angle = angle

print("Angle: {}   Maximum area: {}".format(relevant_angle, max_area))

# Part 2 of challengr. A job for trig!

def hypoteneus(a):
    hyp = math.sqrt(a)
    return hyp


min_length = 100000
town_a = 20
town_b = 30
river = 100
for x in range(1, 101):
    first = x ** 2 + town_a ** 2
    second = (river -x) ** 2 + town_b ** 2

    first_pipe = hypoteneus(first)
    second_pipe = hypoteneus(second)
    total_pipe = first_pipe + second_pipe
    if total_pipe < min_length:
        min_length = total_pipe
        location = x

print("Location: ", location)