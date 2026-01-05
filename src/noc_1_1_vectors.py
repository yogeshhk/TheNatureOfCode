# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example 1-1: Vectors
# PyP5 port by: Yogesh Kulkarni
# Updated by : Akanksha Suneri
# Migrated to py5
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/chp01_vectors/NOC_1_1_bouncingball_novectors
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=7

import py5
x = 100
y = 100
xspeed = 2.5
yspeed = 2


def setup():
    py5.size(800, 200)
    # smooth() # Not Implemented


def draw():
    py5.background(255)
    # Add the current speed to the location.
    global x, y, xspeed, yspeed
    x = x + xspeed
    y = y + yspeed
    if (x > py5.width) or (x < 0):
        xspeed = xspeed * -1
    if (y > py5.height) or (y < 0):
        yspeed = yspeed * -1
    # Display circle at x location
    py5.stroke(0)
    py5.stroke_weight(2)
    py5.fill(127)
    py5.ellipse(x, y, 48, 48)

if __name__ == "__main__":
    py5.run_sketch()